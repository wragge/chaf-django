from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Article(models.Model):
	issue_date = models.DateField()
	page = models.CharField(max_length=20, blank=True, null=True)
	page_column = models.CharField(max_length=20, blank=True, null=True)
	title = models.CharField(max_length=250, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	source = models.CharField(max_length=50, blank=True, null=True)

	def get_absolute_url(self):
		return reverse('article-view', kwargs={'id': self.id})