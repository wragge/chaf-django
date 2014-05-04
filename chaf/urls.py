from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from chaf.tungwah.views import *
from chaf.threads.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chaf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name="home"),
)

urlpatterns += patterns('chaf.tungwah.views',
	url(r'^tungwah/$', HomePageView.as_view(), name="tungwah-home"),
    url(r'^tungwah/articles/$', ArticleSearchView.as_view(), name="article_list"),
    url(r'^tungwah/articles/results\.(?P<fmt>(html|rdf|json|ttl))/$', ArticleSearchView.as_view()),
    url(r'^tungwah/articles/(?P<id>\d+)\.(?P<fmt>(html|rdf|json|ttl))/$', ArticleView.as_view()),
    url(r'^tungwah/articles/(?P<id>\d+)/$', ArticleView.as_view(), name='article-view'),
    url(r'^tungwah/issues/$', IssueListView.as_view(), name="issue_list"),
    url(r'^tungwah/issues/(?P<year>\d{4})/$', IssueListView.as_view(), name="issue_list_year"),
    url(r'^tungwah/issues/results\.(?P<fmt>(html|rdf|json|ttl))/$', IssueListView.as_view()),
    url(r'^tungwah/issues/(?P<year>\d{4})/results\.(?P<fmt>(html|rdf|json|ttl))/$', IssueListView.as_view()),
    url(r'^tungwah/issues/(?P<id>\d{4}-\d{2}-\d{2})\.(?P<fmt>(html|rdf|json|ttl))/$', IssueView.as_view()),
    url(r'^tungwah/issues/(?P<id>\d{4}-\d{2}-\d{2})/$', IssueView.as_view(), name='issue-view'),
    #url(r'^residents/add/$', ResidentCreate.as_view(), name='resident-add'),
    #url(r'^residents/update/(?P<pk>\d+)/$', ResidentUpdate.as_view(), name='resident-update'),
    #url(r'^residents/delete/(?P<id>\d+)/$', ResidentDelete.as_view(), name='resident_delete'),
    #url(r'^residents/(?P<resident_id>\d+)/name/create/$', ResidentNameCreate.as_view(), name='resident-name-add'),
    #url(r'^residents/name/(?P<pk>\d+)/update/$', ResidentNameUpdate.as_view(), name='resident-name-update'),
)

urlpatterns += patterns('chaf.threads.views',
    url(r'^threads/$', HomePageView.as_view(), name="threads-home"),
    url(r'^threads/registrations/$', ThreadsSearchView.as_view(), name="registration-list"),
    url(r'^threads/registrations/results\.(?P<fmt>(html|rdf|json|ttl))/$', ThreadsSearchView.as_view()),
    url(r'^threads/births/(?P<id>\d+)\.(?P<fmt>(html|rdf|json|ttl))/$', BirthRegistrationView.as_view()),
    url(r'^threads/births/(?P<id>\d+)/$', BirthRegistrationView.as_view(), name='birth-view'),
    url(r'^threads/marriages/(?P<id>\d+)\.(?P<fmt>(html|rdf|json|ttl))/$', MarriageRegistrationView.as_view()),
    url(r'^threads/marriages/(?P<id>\d+)/$', MarriageRegistrationView.as_view(), name='marriage-view'),
    url(r'^threads/issues/$', IssueListView.as_view(), name="issue_list"),
    url(r'^threads/issues/(?P<year>\d{4})/$', IssueListView.as_view(), name="issue_list_year"),
    url(r'^threads/issues/results\.(?P<fmt>(html|rdf|json|ttl))/$', IssueListView.as_view()),
    url(r'^threads/issues/(?P<year>\d{4})/results\.(?P<fmt>(html|rdf|json|ttl))/$', IssueListView.as_view()),
    url(r'^threads/issues/(?P<id>\d{4}-\d{2}-\d{2})\.(?P<fmt>(html|rdf|json|ttl))/$', IssueView.as_view()),
    url(r'^threads/issues/(?P<id>\d{4}-\d{2}-\d{2})/$', IssueView.as_view(), name='issue-view'),
    #url(r'^residents/add/$', ResidentCreate.as_view(), name='resident-add'),
    #url(r'^residents/update/(?P<pk>\d+)/$', ResidentUpdate.as_view(), name='resident-update'),
    #url(r'^residents/delete/(?P<id>\d+)/$', ResidentDelete.as_view(), name='resident_delete'),
    #url(r'^residents/(?P<resident_id>\d+)/name/create/$', ResidentNameCreate.as_view(), name='resident-name-add'),
    #url(r'^residents/name/(?P<pk>\d+)/update/$', ResidentNameUpdate.as_view(), name='resident-name-update'),
)
