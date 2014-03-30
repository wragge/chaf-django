# Create your views here.
import httplib
import itertools
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.utils.cache import patch_vary_headers
from django.contrib.sites.models import Site
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rdflib import Graph
from rdflib import Namespace, BNode, Literal, RDF, URIRef
from django_conneg.views import ContentNegotiatedView
from django_conneg.decorators import renderer
from haystack.query import EmptySearchQuerySet
from haystack.forms import SearchForm

from linkeddata.models import *

SCHEMAS = {
            'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
            'owl': 'http://www.w3.org/2002/07/owl#',
            'foaf': 'http://xmlns.com/foaf/0.1/',
            'dc': 'http://purl.org/dc/terms/',
            'bio': 'http://purl.org/vocab/bio/0.1/',
            'geo': 'http://www.w3.org/2003/01/geo/wgs84_pos#',
            'rel': 'http://purl.org/vocab/relationship/',
            }


class LinkedDataView(ContentNegotiatedView):
    model = None
    path = ''
    template_name = ''

    def get(self, request, id=None, fmt=None):
        context = {}
        if fmt:
            context['content'] = self.get_item(id)
            context['extra'] = self.get_extra(id)
            return self.render_to_format(request, context, self.template_name, fmt)
        else:
            context['status_code'] = 303
            context['additional_headers'] = {'location': self.path % id}
            context['content'] = None
            return self.render(request, context, self.template_name)

    def get_extra(self, id):
        return {}

    def get_item(self, id):
        result = self.model.objects.select_related().get(id=id)
        return result

    def get_namespaces(self, graph):
        namespaces = {}
        schemas = RDFSchema.objects.all()
        for schema in schemas:
            namespace = Namespace(schema.uri)
            graph.bind(schema.prefix, namespace)
            namespaces[schema.prefix] = namespace
        return namespaces

    def render(self, request, context, template_name):
        """
        Returns a HttpResponse of the right media type as specified by the
        request.
        context can contain status_code and additional_headers members, to set
        the HTTP status code and headers of the request, respectively.
        template_name should lack a file-type suffix (e.g. '.html', as
        renderers will append this as necessary.
        """
        request, context, template_name = self.get_render_params(request, context, template_name)
        self.set_renderers()

        status_code = context.pop('status_code', httplib.OK)
        additional_headers = context.pop('additional_headers', {})

        for renderer in request.renderers:
            response = renderer(request, context, template_name)
            if response is NotImplemented:
                continue
            response.status_code = status_code
            response.renderer = renderer
            break
        else:
            tried_mimetypes = list(itertools.chain(*[r.mimetypes for r in request.renderers]))
            response = self.http_not_acceptable(request, tried_mimetypes)
            response.renderer = None

        for key, value in additional_headers.iteritems():
            # My changes -- Modify location for 303 redirect
            if key == 'location' and response.renderer:
                location = '%s.%s/' % (value, response.renderer.format)
                try:
                    location += '?%s' % context['params']
                except KeyError:
                    pass
                try:
                    location += '?page=%s' % context['page']
                except KeyError:
                    pass
                response[key] = location
            else:
                response[key] = value
            # End my changes

        # We're doing content-negotiation, so tell the user-agent that the
        # response will vary depending on the accept header.
        patch_vary_headers(response, ('Accept',))
        return response

    @renderer(format='html', mimetypes=('text/html', 'application/xhtml+xml'), name='HTML', priority=1)
    def render_html(self, request, context, template_name):
        if context['content']:
            template_name = self.join_template_name(template_name, 'html')
            identifier = 'http://%s%s' % (Site.objects.get_current().domain, context['content'].get_absolute_url())
            context['identifier'] = identifier
            context['id_path'] = identifier[:-1]
            return render_to_response(template_name, context, context_instance=RequestContext(request), content_type='text/html')
        else:
            return HttpResponse(content='')

    @renderer(format='json', mimetypes=('application/json',), name='JSON')
    def render_json(self, request, context, template_name):
        if context['content']:
            #data = {'name': context['memorial'].name}
            graph = self.make_graph(context['content'])
            return HttpResponse(graph.serialize(format='json-ld', indent=4), content_type='application/json')
        else:
            return HttpResponse(content='')

    @renderer(format='rdf', mimetypes=('application/rdf+xml',), name='RDF')
    def render_rdf(self, request, context, template_name):
        if context['content']:
            graph = self.make_graph(context['content'])
            return HttpResponse(graph.serialize(format='pretty-xml'), content_type='application/rdf+xml')
        else:
            return HttpResponse(content='')

    @renderer(format='ttl', mimetypes=('text/turtle',), name='TURTLE')
    def render_ttl(self, request, context, template_name):
        if context['content']:
            graph = self.make_graph(context['content'])
            return HttpResponse(graph.serialize(format='turtle'), content_type='text/turtle')
        else:
            return HttpResponse(content='')


class LinkedDataListView(LinkedDataView):

    def get(self, request, fmt=None, **kwargs):
        context = {}
        if fmt:
            results = self.get_results()
            paginator = Paginator(results, 25)
            page = request.GET.get('page', '1')
            try:
                content = paginator.page(page)
            except PageNotAnInteger:
                content = paginator.page(1)
            except EmptyPage:
                content = paginator.page(paginator.num_pages)
            context['content'] = content
            return self.render_to_format(request, context, self.template_name, fmt)
        else:
            context['page'] = request.GET.get('page', '1')
            context['status_code'] = 303
            context['additional_headers'] = {'location': self.path}
            context['content'] = None
            return self.render(request, context, self.template_name)

    def get_results(self):
        results = self.model.objects.select_related().all()
        return results

    def get_namespaces(self, graph):
        namespaces = {}
        schemas = RDFSchema.objects.all()
        for schema in schemas:
            namespace = Namespace(schema.uri)
            graph.bind(schema.prefix, namespace)
            namespaces[schema.prefix] = namespace
        return namespaces

    @renderer(format='html', mimetypes=('text/html', 'application/xhtml+xml'), name='HTML', priority=1)
    def render_html(self, request, context, template_name):
        if context['content'] != None:
            template_name = self.join_template_name(template_name, 'html')
            identifier = 'http://%s%s/' % (Site.objects.get_current().domain, self.path)
            context['identifier'] = identifier
            context['id_path'] = identifier[:-1]
            return render_to_response(template_name, context, context_instance=RequestContext(request), mimetype='text/html')
        else:
            return HttpResponse(content='')

class LinkedDataSearchView(LinkedDataView):
    searchqueryset = None
    form_class = SearchForm
    params = [{'name': 'q', 'default': ''}, {'name': 'page', 'default': 1}, {'name': 'order_by', 'default': None}]
    default_order = 'date'
    facets = []

    def get(self, request, fmt=None):
        context = {}
        if fmt:
            query = ''
            results = EmptySearchQuerySet()
            form = self.form_class(request.GET, searchqueryset=self.searchqueryset, load_all=True)
            if form.is_valid():
                print form.cleaned_data
                query = form.cleaned_data['q']
                order_by = request.GET.get('order_by', None)
                results = form.search(order_by)
            else:
                results = form.no_query_found()
            if self.facets:
                for facet in self.facets:
                    results = results.facet(facet, mincount=1, sort='index')
                context['facets'] = results.facet_counts()
            paginator = Paginator(results, 25)
            page = request.GET.get('page', '1')
            try:
                content = paginator.page(page)
            except PageNotAnInteger:
                content = paginator.page(1)
            except EmptyPage:
                content = paginator.page(paginator.num_pages)
            context['content'] = content
            context['paginator'] = paginator
            context['query'] = query
            context['form'] = form
            return self.render_to_format(request, context, self.template_name, fmt)
        else:
            params = []
            if request.GET.get('q') == '' and not request.GET.get('order_by'):
                params.append('order_by={}'.format(self.default_order))
            for param in self.params:
                print param['name']
                param_value = request.GET.get(param['name'], param['default'])
                if param_value:
                    params.append('{}={}'.format(param['name'], param_value))
            print params
            context['params'] = '&'.join(params)
            context['status_code'] = 303
            context['additional_headers'] = {'location': self.path}
            context['content'] = None
            return self.render(request, context, self.template_name)

    def get_namespaces(self, graph):
        namespaces = {}
        schemas = RDFSchema.objects.all()
        for schema in schemas:
            namespace = Namespace(schema.uri)
            graph.bind(schema.prefix, namespace)
            namespaces[schema.prefix] = namespace
        return namespaces

    @renderer(format='html', mimetypes=('text/html', 'application/xhtml+xml'), name='HTML', priority=1)
    def render_html(self, request, context, template_name):
        if context['content'] != None:
            template_name = self.join_template_name(template_name, 'html')
            identifier = 'http://%s%s/' % (Site.objects.get_current().domain, self.path)
            context['identifier'] = identifier
            context['id_path'] = identifier[:-1]
            return render_to_response(template_name, context, context_instance=RequestContext(request), mimetype='text/html')
        else:
            return HttpResponse(content='')
