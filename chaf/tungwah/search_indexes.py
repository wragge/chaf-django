from haystack import indexes

from chaf.tungwah.models import Article

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	issue_date = indexes.DateField(model_attr='issue_date', faceted=True)
	year = indexes.IntegerField(faceted=True)

	def prepare_year(self, obj):
		return obj.issue_date.year

	def get_model(self):
		return Article