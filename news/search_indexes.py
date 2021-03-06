import datetime
from haystack import indexes
from .models import New


class NewsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, )
    author = indexes.CharField(model_attr='author', faceted=True, )
    content = indexes.CharField(model_attr='content', )
    created_date = indexes.DateField(model_attr='created_date', faceted=True, )
    place = indexes.CharField(model_attr='place', faceted=True)
    title = indexes.CharField(model_attr='title', )
    sorted_name = indexes.CharField(model_attr='title', indexed=False, stored=True)
    times_viewed = indexes.IntegerField(model_attr='times_viewed', )

    def get_model(self):
        return New

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(created_date__lte=datetime.datetime.now())