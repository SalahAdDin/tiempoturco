import json

from django.views.generic import ListView

from actions import week_range
import datetime

from .models import KeyWord, Topic, Subtopic
from news.models import New
from visuals.models import Gallery, Image, Video


# Mixin
class MenuMixin(object):
    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        context = super(MenuMixin, self).get_context_data(**kwargs)
        context['rnews'] = New.objects.order_by('-times_viewed').filter(is_published=True)[:3]  # Noticias recomendadas
        context['lnews'] = New.objects.filter(is_published=True).all()[:5]    # Mas noticias
        context['mnews'] = New.objects.order_by('topic').filter(is_published=True)[:10]
        context['latest'] = New.objects.filter(is_published=True).all()[:20]
        context['local'] = New.objects.filter(is_published=True).filter(subtopic__slug='local')[:20]
        context['featured'] = New.objects.order_by('-times_viewed').filter(is_published=True).filter(created_date__year=today.year).filter(created_date__month=today.month)[:20]
        context['images'] = Image.objects.order_by('-created_date').filter(gallery__isnull=True)[:10]
        context['videos'] = Video.objects.order_by('-created_date')[:10]
        context['gallerys'] = Gallery.objects.order_by('-created_date')[:20]
        return context

# Create your views here.


# Vista basica para Palabras Clave
class KeyWordsNewsView(MenuMixin, ListView):
    template_name = 'keywords_news.html'
    paginate_by = 15
    model = New
    name_field = 'slug'

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get('slug')
        key = KeyWord.objects.get(slug=slug)
        context = super(KeyWordsNewsView, self).get_context_data(**kwargs)
        context['name'] = key.name
        return context

    def get_queryset(self):
        key = self.kwargs.get('slug')
        return self.model.objects.filter(keywords__slug__iexact=key).filter(is_published=True)


class KeyWordsIndexView(MenuMixin, ListView):
    template_name = 'keywords_index.html'
    paginate_by = 150
    model = KeyWord


# Vista basica para Tema
class TopicNewsView(MenuMixin, ListView):
    template_name = 'topic_news.html'
    paginate_by = 5
    model = New
    name_field = 'slug'

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get('slug')
        topic = Topic.objects.get(slug=slug)
        context = super(TopicNewsView, self).get_context_data(**kwargs)
        context['name'] = topic.name
        return context

    def get_queryset(self):
        topic = self.kwargs.get('slug')
        return self.model.objects.filter(topic__slug=topic).filter(is_published=True)


# Vista basica para Subtema
class SubTopicNewsView(MenuMixin, ListView):
    template_name = 'topic_news.html'
    paginate_by = 5
    model = New
    name_field = 'slug'

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get('slug')
        subtopic = Subtopic.objects.get(slug=slug)
        context = super(SubTopicNewsView, self).get_context_data(**kwargs)
        context['name'] = subtopic.name
        return context

    def get_queryset(self):
        subtopic = self.kwargs.get('slug')
        return self.model.objects.filter(subtopic__slug=subtopic).filter(is_published=True)