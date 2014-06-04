from django.shortcuts import render
from django.views.generic.base import TemplateView
from linkeddata.views import LinkedDataView, LinkedDataListView, LinkedDataSearchView
from linkeddata.models import *
from rdflib import Graph
from rdflib import Namespace, BNode, Literal, RDF, URIRef
from haystack.query import SearchQuerySet
from chaf.threads.models import BirthRegistration, MarriageRegistration
from chaf.threads.forms import ThreadsSearchForm


class ThreadsHomePageView(TemplateView):
    template_name = "threads/home.html"

class BirthRegistrationView(LinkedDataView):
	model = BirthRegistration
	path = '/threads/births/%s'
	template_name = 'threads/birth'

class BirthRegistrationListView(LinkedDataListView):
    model = BirthRegistration
    path = '/threads/births/results'
    template_name = 'threads/births'

class MarriageRegistrationView(LinkedDataView):
	model = MarriageRegistration
	path = '/threads/marriages/%s'
	template_name = 'threads/marriage'

class MarriageRegistrationListView(LinkedDataListView):
    model = MarriageRegistration
    path = '/threads/marriages/results'
    template_name = 'threads/marriages'

class ThreadsSearchView(LinkedDataSearchView):
    form_class = ThreadsSearchForm
    path = '/threads/registrations/results'
    template_name = 'threads/registrations'
    params = [{'name': 'q', 'default': ''}, {'name': 'page', 'default': 1}, {'name': 'year', 'default': None}, {'name': 'order_by', 'default': None}]
    default_order = 'alpha_sort'
    searchqueryset = SearchQuerySet().models(BirthRegistration, MarriageRegistration)
    facets = [('type', 'count'), ('place', 'count'), ('year', 'index')]