from django.db import models
from django.core.urlresolvers import reverse
from django.template import defaultfilters
import re

# Create your models here.


class Article(models.Model):
    issue_date = models.DateField()
    page = models.CharField(max_length=20, blank=True, null=True)
    page_column = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        if self.title:
            title = self.title
        else:
            title = defaultfilters.truncatewords(self.description, 10)
        return title

    def get_absolute_url(self):
        return reverse('article-view', kwargs={'id': self.id})

    def get_page_url(self):
        if self.page.lower()[:3] == 'sup':
            page_num = '1 S'
        else:
            try:
                page_num = re.search(r'(\d+)', self.page).group(1)
            except AttributeError:
                page_num = None
        if page_num:
            try:
                page = Page.objects.get(issue_date=self.issue_date, page=page_num)
            except Article.DoesNotExist:
                page_url = None
            else:
                page_url = page.url
        else:
            page_url = None
        return page_url


class Page(models.Model):
    issue_date = models.DateField()
    page = models.CharField(max_length=20, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
