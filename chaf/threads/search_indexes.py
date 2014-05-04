from haystack import indexes

from chaf.threads.models import BirthRegistration, MarriageRegistration

class BirthRegistrationIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(use_template=True, boost=1.5)
	index_child_surname = indexes.CharField(model_attr='index_child_surname')
	index_child_firstname = indexes.CharField(model_attr='index_child_firstname')
	index_father_firstname = indexes.CharField(model_attr='index_father_firstname')
	index_mother_firstname = indexes.CharField(model_attr='index_mother_firstname')
	year = indexes.IntegerField(model_attr='index_year', faceted=True)
	place = indexes.CharField(model_attr='index_registration_place', faceted=True)
	reg_number = indexes.CharField(model_attr='reg_number')
	reg_year = indexes.CharField(model_attr='reg_year')
	alpha_sort = indexes.CharField()
	type = indexes.CharField(faceted=True)

	def prepare_alpha_sort(self, obj):
		sort_string = '{}{}'.format(obj.index_child_surname, obj.index_child_firstname)
		return sort_string.lower().replace(' ', '').replace('-', '')

	def prepare_type(self, obj):
		return 'birth'

	def get_model(self):
		return BirthRegistration


class MarriageRegistrationIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(use_template=True, boost=1.5)
	index_spouse1_surname = indexes.CharField(model_attr='index_spouse1_surname')
	index_spouse1_firstname = indexes.CharField(model_attr='index_spouse1_firstname')
	index_spouse2_surname = indexes.CharField(model_attr='index_spouse2_surname')
	index_spouse2_firstname = indexes.CharField(model_attr='index_spouse2_firstname')
	year = indexes.IntegerField(model_attr='index_year', faceted=True)
	place = indexes.CharField(model_attr='index_registration_place', faceted=True)
	reg_number = indexes.CharField(model_attr='reg_number')
	reg_year = indexes.CharField(model_attr='reg_year')
	alpha_sort = indexes.CharField()
	type = indexes.CharField(faceted=True)

	def prepare_alpha_sort(self, obj):
		sort_string = '{}{}{}{}'.format(obj.index_spouse1_surname, obj.index_spouse1_firstname, obj.index_spouse2_surname, obj.index_spouse2_firstname)
		return sort_string.lower().replace(' ', '').replace('-', '')

	def prepare_type(self, obj):
		return 'marriage'

	def get_model(self):
		return MarriageRegistration