from django.contrib.sites.models import Site
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.db.models import Count
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from django.template import defaultfilters
from isodate import parse_date
import datetime
from linkeddata.views import LinkedDataView, LinkedDataListView, LinkedDataSearchView
from linkeddata.models import *
from rdflib import Graph
from rdflib import Namespace, BNode, Literal, RDF, URIRef
from django_conneg.decorators import renderer
from chaf.tungwah.models import *
from chaf.tungwah.forms import *


class HomePageView(TemplateView):

    template_name = "tungwah/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        articles = Article.objects.all().order_by('?')
        context['num_articles'] = len(articles)
        context['article'] = articles[0]
        context['num_issues'] = Article.objects.values_list('issue_date', flat=True).distinct().count()
        return context


class NewspaperView(LinkedDataView):

    def make_newspaper_nodes(self, date, graph, namespaces):
        if date < datetime.date(1902, 8, 16):
            this_newspaper = URIRef('http://trove.nla.gov.au/version/16575625')
            newspaper = 'Tung Wah News'
            graph.add((this_newspaper, namespaces['schema']['name'], Literal('The Tung Wah News')))
        else:
            this_newspaper = URIRef('http://trove.nla.gov.au/version/16567400')
            newspaper = 'Tung Wah Times'
            graph.add((this_newspaper, namespaces['schema']['name'], Literal('The Tung Wah Times')))
        graph.add((this_newspaper, namespaces['rdf']['type'], namespaces['schema']['Organization']))
        graph.add((this_newspaper, namespaces['rdf']['type'], namespaces['bibo']['Newspaper']))
        return (this_newspaper, newspaper, graph)


class ArticleView(NewspaperView):
    model = Article
    path = '/tungwah/articles/%s'
    template_name = 'tungwah/article'

    def make_graph(self, entity):
        graph = Graph()
        namespaces = self.get_namespaces(graph)
        host_ns = Namespace('http://%s' % (Site.objects.get_current().domain))
        this_article = URIRef(host_ns[entity.get_absolute_url()])
        graph.add((this_article, namespaces['rdf']['type'], namespaces['schema']['NewsArticle']))
        graph.add((this_article, namespaces['rdfs']['label'], Literal(str(entity))))
        graph.add((this_article, namespaces['schema']['name'], Literal(str(entity))))
        graph.add((this_article, namespaces['schema']['description'], Literal(str(entity.description))))
        graph.add((this_article, namespaces['schema']['printPage'], Literal(str(entity.page))))
        graph.add((this_article, namespaces['schema']['printColumn'], Literal(str(entity.page_column))))
        graph.add((this_article, namespaces['schema']['datePublished'], Literal(str(entity.issue_date))))
        this_newspaper, newspaper, graph = self.make_newspaper_nodes(entity.issue_date, graph, namespaces)
        graph.add((this_article, namespaces['schema']['provider'], this_newspaper))
        this_issue = URIRef(host_ns['/tungwah/issues/{}/'.format(entity.issue_date)])
        graph.add((this_article, namespaces['dcterms']['isPartOf'], this_issue))
        return graph


class IssueView(NewspaperView):
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

    def make_graph(self, entity):
        graph = Graph()
        namespaces = self.get_namespaces(graph)
        host_ns = Namespace('http://%s' % (Site.objects.get_current().domain))
        this_issue = URIRef(host_ns['/tungwah/issues/{}/'.format(entity['issue'])])
        this_newspaper, newspaper, graph = self.make_newspaper_nodes(entity['issue'], graph, namespaces)
        f_date = defaultfilters.date(entity['issue'], 'j F Y')
        graph.add((this_issue, namespaces['rdf']['type'], namespaces['schema']['CreativeWork']))
        graph.add((this_issue, namespaces['rdf']['type'], namespaces['dcterms']['Issue']))
        graph.add((this_issue, namespaces['rdfs']['label'], Literal('{}, {}'.format(newspaper, f_date))))
        graph.add((this_issue, namespaces['schema']['datePublished'], Literal(str(entity['issue']))))
        graph.add((this_issue, namespaces['schema']['provider'], this_newspaper))
        for article in entity['articles']:
            graph.add((this_issue, namespaces['dcterms']['hasPart'], URIRef(host_ns[article.get_absolute_url()])))
        return graph

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

    def make_graph(self, entity):
        graph = Graph()
        namespaces = self.get_namespaces(graph)
        host_ns = Namespace('http://%s' % (Site.objects.get_current().domain))
        news = URIRef('http://trove.nla.gov.au/version/16575625')
        graph.add((news, namespaces['schema']['name'], Literal('The Tung Wah News')))
        times = URIRef('http://trove.nla.gov.au/version/16567400')
        graph.add((times, namespaces['schema']['name'], Literal('The Tung Wah Times')))
        graph.add((news, namespaces['rdf']['type'], namespaces['schema']['Organization']))
        graph.add((news, namespaces['rdf']['type'], namespaces['bibo']['Newspaper']))
        graph.add((times, namespaces['rdf']['type'], namespaces['schema']['Organization']))
        graph.add((times, namespaces['rdf']['type'], namespaces['bibo']['Newspaper']))
        for article in entity.object_list:
            this_article = URIRef(host_ns[article.object.get_absolute_url()])
            if article.object.issue_date < datetime.date(1902, 8, 16):
                graph.add((news, namespaces['dcterms']['hasPart'], this_article))
            else:
                graph.add((times, namespaces['dcterms']['hasPart'], this_article))
        return graph


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

    def make_graph(self, entity):
        graph = Graph()
        namespaces = self.get_namespaces(graph)
        host_ns = Namespace('http://%s' % (Site.objects.get_current().domain))
        news = URIRef('http://trove.nla.gov.au/version/16575625')
        graph.add((news, namespaces['schema']['name'], Literal('The Tung Wah News')))
        times = URIRef('http://trove.nla.gov.au/version/16567400')
        graph.add((times, namespaces['schema']['name'], Literal('The Tung Wah Times')))
        graph.add((news, namespaces['rdf']['type'], namespaces['schema']['Organization']))
        graph.add((news, namespaces['rdf']['type'], namespaces['bibo']['Newspaper']))
        graph.add((times, namespaces['rdf']['type'], namespaces['schema']['Organization']))
        graph.add((times, namespaces['rdf']['type'], namespaces['bibo']['Newspaper']))
        for issue in entity.object_list:
            this_issue = URIRef(host_ns['/tungwah/issues/{}/'.format(issue['issue_date'])])
            if issue['issue_date'] < datetime.date(1902, 8, 16):
                graph.add((news, namespaces['dcterms']['hasPart'], this_issue))
            else:
                graph.add((times, namespaces['dcterms']['hasPart'], this_issue))
        return graph


