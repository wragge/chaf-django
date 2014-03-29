from django.contrib.sites.models import Site
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.db.models import Count
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from isodate import parse_date
import datetime
from linkeddata.views import LinkedDataView, LinkedDataListView, LinkedDataSearchView
from linkeddata.models import *
from rdflib import Graph
from rdflib import Namespace, BNode, Literal, RDF, URIRef
from django_conneg.decorators import renderer
from chaf.tungwah.models import *
from chaf.tungwah.forms import *

NEWSPAPERS = {
    'title': 'Tung Wah Times',
    'url': 'http://trove.nla.gov.au/version/16567400',

}


class HomePageView(TemplateView):

    template_name = "tungwah/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        articles = Article.objects.all().order_by('?')
        context['num_articles'] = len(articles)
        context['article'] = articles[0]
        context['num_issues'] = Article.objects.values_list('issue_date', flat=True).distinct().count()
        return context


class ArticleView(LinkedDataView):
    model = Article
    path = '/tungwah/articles/%s'
    template_name = 'tungwah/article'

    def make_graph(self, entity):
        namespaces = {}
        graph = Graph()
        schemas = RDFSchema.objects.all()
        for schema in schemas:
            namespace = Namespace(schema.uri)
            graph.bind(schema.prefix, namespace)
            namespaces[schema.prefix] = namespace
        host_ns = Namespace('http://%s' % (Site.objects.get_current().domain))
        this_article = URIRef(host_ns[entity.get_absolute_url()])
        graph.add((this_article, namespaces['rdf']['type'], namespaces['schema']['NewsArticle']))
        graph.add((this_article, namespaces['rdfs']['label'], Literal(str(entity))))
        graph.add((this_article, namespaces['schema']['name'], Literal(str(entity))))
        graph.add((this_article, namespaces['schema']['description'], Literal(str(entity.description))))
        graph.add((this_article, namespaces['schema']['printPage'], Literal(str(entity.page))))
        graph.add((this_article, namespaces['schema']['printColumn'], Literal(str(entity.page_column))))
        graph.add((this_article, namespaces['schema']['datePublished'], Literal(str(entity.issue_date))))
        print entity.issue_date
        if entity.issue_date < datetime.date(1902, 8, 16):
            this_newspaper = URIRef('http://trove.nla.gov.au/version/16575625')
            graph.add((this_newspaper, namespaces['schema']['name'], Literal('The Tung Wah News')))
        else:
            this_newspaper = URIRef('http://trove.nla.gov.au/version/16567400')
            graph.add((this_newspaper, namespaces['schema']['name'], Literal('The Tung Wah Times')))
        graph.add((this_newspaper, namespaces['rdf']['type'], namespaces['schema']['Organization']))
        graph.add((this_newspaper, namespaces['rdf']['type'], namespaces['bibo']['Newspaper']))
        graph.add((this_article, namespaces['schema']['provider'], this_newspaper))
        return graph


class IssueView(LinkedDataView):
    model = Article
    path = '/tungwah/issues/%s'
    template_name = 'tungwah/issue'

    def get_item(self, id):
        articles = self.model.objects.filter(issue_date=id).order_by('page', 'page_column')
        return {'issue': parse_date(id), 'articles': articles}

    @renderer(format='html', mimetypes=('text/html', 'application/xhtml+xml'), name='HTML', priority=1)
    def render_html(self, request, context, template_name):
        if context['content']:
            template_name = self.join_template_name(template_name, 'html')
            identifier = 'http://%s%s' % (Site.objects.get_current().domain, context['content']['issue'])
            context['identifier'] = identifier
            #context['id_path'] = identifier[:-1]
            return render_to_response(template_name, context, context_instance=RequestContext(request), content_type='text/html')
        else:
            return HttpResponse(content='')

class ArticleListView(LinkedDataListView):
    model = Article
    path = '/tungwah/articles/results'
    template_name = 'tungwah/articles'

    def make_graph(self, entities):
        namespaces = {}
        graph = Graph()
        schemas = RDFSchema.objects.all()
        for schema in schemas:
            namespace = Namespace(schema.uri)
            graph.bind(schema.prefix, namespace)
            namespaces[schema.prefix] = namespace
        host_ns = Namespace('http://%s' % (Site.objects.get_current().domain))
        for entity in entities:
            this_person = URIRef(host_ns[entity.get_absolute_url()])
            graph.add((this_person, namespaces['rdf']['type'], namespaces['foaf']['Person']))
            graph.add((this_person, namespaces['rdfs']['label'], Literal(str(entity))))
        return graph

class ArticleSearchView(LinkedDataSearchView):
    form_class = ArticleSearchForm
    path = '/tungwah/articles/results'
    template_name = 'tungwah/articles'
    params = [{'name': 'q', 'default': ''}, {'name': 'page', 'default': 1}, {'name': 'year', 'default': None}, {'name': 'order_by', 'default': None}]
    default_order = 'issue_date'
    facets = ['year']


class IssueListView(LinkedDataListView):
    model = Article
    path = '/tungwah/issues/{}results'
    template_name = 'tungwah/issues'

    def get(self, request, fmt=None, **kwargs):
        context = {}
        year = kwargs.get('year', None)
        self.path = self.path.format('{}/'.format(year) if year else '')
        if fmt:
            results = self.get_results(year)
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

    def get_results(self, year):
        if year:
            results = self.model.objects.filter(issue_date__year=year).values('issue_date').annotate(num_articles=Count('issue_date')).distinct().order_by('issue_date')
        else:
            results = self.model.objects.values('issue_date').annotate(num_articles=Count('issue_date')).distinct().order_by('issue_date')
        return results


