from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Location(models.Model):
	street_number_master = models.CharField(max_length=10, blank=True, null=True)
	street_number_source = models.CharField(max_length=10, blank=True, null=True)
	street_name_source = models.CharField(max_length=100, blank=True, null=True)
	street_name_master = models.CharField(max_length=100, blank=True, null=True)
	business_name = models.TextField(blank=True, null=True)
	economic_activity = models.TextField(blank=True, null=True)
	year = models.IntegerField(blank=True, null=True)
	source = models.CharField(max_length=20, blank=True, null=True)
