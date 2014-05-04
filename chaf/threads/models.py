from django.db import models
from django.core.urlresolvers import reverse

# Create your models here


class MarriageRegistration(models.Model):
	reg_number = models.CharField(max_length=20)
	reg_year = models.IntegerField()
	#Index
	index_spouse1_surname = models.CharField(max_length=50, blank=True, null=True)
	index_spouse1_firstname = models.CharField(max_length=50, blank=True, null=True)
	index_spouse2_surname = models.CharField(max_length=50, blank=True, null=True)
	index_spouse2_firstname = models.CharField(max_length=50, blank=True, null=True)
	index_year = models.IntegerField(blank=True, null=True)
	index_registration_place = models.CharField(max_length=50, blank=True, null=True)
	#Registration
	marriage_date = models.DateField(blank=True, null=True)
	marriage_place = models.CharField(max_length=200, blank=True, null=True)
	marriage_church = models.CharField(max_length=200, blank=True, null=True)
	celebrant_name = models.CharField(max_length=200, blank=True, null=True)
	witnesses = models.CharField(max_length=200, blank=True, null=True)
	#Husband
	husband_surname = models.CharField(max_length=50, blank=True, null=True)
	husband_firstname = models.CharField(max_length=50, blank=True, null=True)
	husband_occupation = models.CharField(max_length=200, blank=True, null=True)
	husband_residence = models.CharField(max_length=200, blank=True, null=True)
	husband_status = models.CharField(max_length=50, blank=True, null=True)
	husband_birthplace = models.CharField(max_length=200, blank=True, null=True)
	husband_birthdate = models.CharField(max_length=50, blank=True, null=True)
	husband_age = models.CharField(max_length=50, blank=True, null=True)
	husband_father_name = models.CharField(max_length=50, blank=True, null=True)
	husband_father_occupation = models.CharField(max_length=200, blank=True, null=True)
	husband_mother_name = models.CharField(max_length=50, blank=True, null=True)
	husband_mother_maiden_name = models.CharField(max_length=50, blank=True, null=True)
	husband_mother_occupation = models.CharField(max_length=200, blank=True, null=True)
	#Wife
	wife_surname = models.CharField(max_length=50, blank=True, null=True)
	wife_firstname = models.CharField(max_length=50, blank=True, null=True)
	wife_occupation = models.CharField(max_length=200, blank=True, null=True)
	wife_residence = models.CharField(max_length=200, blank=True, null=True)
	wife_status = models.CharField(max_length=50, blank=True, null=True)
	wife_birthplace = models.CharField(max_length=200, blank=True, null=True)
	wife_birthdate = models.CharField(max_length=50, blank=True, null=True)
	wife_age = models.CharField(max_length=50, blank=True, null=True)
	wife_father_name = models.CharField(max_length=50, blank=True, null=True)
	wife_father_occupation = models.CharField(max_length=200, blank=True, null=True)
	wife_mother_name = models.CharField(max_length=50, blank=True, null=True)
	wife_mother_maiden_name = models.CharField(max_length=50, blank=True, null=True)
	wife_mother_occupation = models.CharField(max_length=200, blank=True, null=True)

	def __unicode__(self):
		return '{}/{}'.format(self.reg_number, self.reg_year)

	def get_absolute_url(self):
		return reverse('marriage-view', kwargs={'id': self.id})


class BirthRegistration(models.Model):
	reg_number = models.CharField(max_length=20)
	reg_year = models.IntegerField()
	#index
	index_child_firstname = models.CharField(max_length=50, blank=True, null=True)
	index_child_surname = models.CharField(max_length=50, blank=True, null=True)
	index_father_firstname = models.CharField(max_length=50, blank=True, null=True)
	index_mother_firstname = models.CharField(max_length=50, blank=True, null=True)
	index_year = models.IntegerField(blank=True, null=True)
	index_registration_place = models.CharField(max_length=50, blank=True, null=True)
	#registration
	child_name = models.CharField(max_length=50, blank=True, null=True)
	child_sex = models.CharField(max_length=2, blank=True, null=True)
	birthdate = models.DateField(blank=True, null=True)
	birthplace = models.CharField(max_length=200, blank=True, null=True)
	informant_name = models.CharField(max_length=200, blank=True, null=True)
	witnesses = models.CharField(max_length=200, blank=True, null=True)
	#father
	father_surname = models.CharField(max_length=50, blank=True, null=True)
	father_firstname = models.CharField(max_length=50, blank=True, null=True)
	father_occupation = models.CharField(max_length=200, blank=True, null=True)
	father_birthplace = models.CharField(max_length=200, blank=True, null=True)
	father_age = models.CharField(max_length=50, blank=True, null=True)
	#mother
	mother_surname = models.CharField(max_length=50, blank=True, null=True)
	mother_firstname = models.CharField(max_length=50, blank=True, null=True)
	mother_maiden_name = models.CharField(max_length=50, blank=True, null=True)
	mother_occupation = models.CharField(max_length=200, blank=True, null=True)
	mother_birthplace = models.CharField(max_length=200, blank=True, null=True)
	mother_age = models.CharField(max_length=50, blank=True, null=True)
	#other
	marriage_date = models.CharField(max_length=50, blank=True, null=True)
	previous_children = models.CharField(max_length=200, blank=True, null=True)

	def __unicode__(self):
		return '{}/{}'.format(self.reg_number, self.reg_year)

	def get_absolute_url(self):
		return reverse('birth-view', kwargs={'id': self.id})

