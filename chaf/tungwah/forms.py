from django import forms
from haystack.forms import SearchForm

class ArticleSearchForm(SearchForm):
	year = forms.IntegerField(required=False)
	order_by = forms.CharField(required=False)
	
	def no_query_found(self):
		sqs = self.searchqueryset.all().order_by('issue_date')

		if self.cleaned_data['year']:
			sqs = sqs.filter(year=self.cleaned_data['year'])

		return sqs

	def search(self, order_by=None):
		if not self.is_valid():
			
			return self.no_query_found()

		if not self.cleaned_data.get('q'):
		    return self.no_query_found()

		sqs = self.searchqueryset.auto_query(self.cleaned_data['q'])

		if self.cleaned_data['year']:
			sqs = sqs.filter(year=self.cleaned_data['year'])

		if self.load_all:
		    sqs = sqs.load_all()

		if order_by:
			sqs = sqs.order_by(order_by)

		return sqs