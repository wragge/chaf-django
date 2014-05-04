from django import forms
from haystack.forms import SearchForm

class ThreadsSearchForm(SearchForm):
	year = forms.IntegerField(required=False)
	order_by = forms.CharField(required=False)
	type = forms.CharField(required=False)
	place = forms.CharField(required=False)
	
	def no_query_found(self):
		sqs = self.searchqueryset.all()
		order_by = self.cleaned_data.get('order_by', 'alpha_sort')
		print order_by
		sqs = sqs.order_by(order_by)

		if self.cleaned_data['year']:
			sqs = sqs.filter(year=self.cleaned_data['year'])

		if self.cleaned_data['place']:
			sqs = sqs.filter(place=self.cleaned_data['place'])

		if self.cleaned_data['type']:
			sqs = sqs.filter(type=self.cleaned_data['type'])

		return sqs

	def search(self, order_by=None):
		if not self.is_valid():
			
			return self.no_query_found()

		if not self.cleaned_data.get('q'):
		    return self.no_query_found()

		q = self.cleaned_data['q']
		#sqs = self.searchqueryset.auto_query(q)
		sqs = self.searchqueryset.auto_query(q)

		if self.cleaned_data['year']:
			sqs = sqs.filter(year=self.cleaned_data['year'])

		if self.cleaned_data['place']:
			sqs = sqs.filter(place=self.cleaned_data['place'])

		if self.cleaned_data['type']:
			sqs = sqs.filter(type=self.cleaned_data['type'])

		if self.load_all:
		    sqs = sqs.load_all()

		if order_by:
			sqs = sqs.order_by(order_by)

		return sqs