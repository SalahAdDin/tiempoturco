from django.views.generic import ListView, DateDetailView
from actions import week_range
import datetime
from haystack.views import FacetedSearchView

from .models import New
from visuals.models import Gallery, Image, Video


# Mixin
class MenuMixin(object):
    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        context = super(MenuMixin, self).get_context_data(**kwargs)
        context['latest'] = self.model.objects.filter(is_published=True).all()[:20]
        context['local'] = self.model.objects.filter(is_published=True).filter(subtopic__slug='local')[:20]
        context['featured'] = self.model.objects.order_by('-times_viewed').filter(is_published=True).filter(created_date__year=today.year).filter(created_date__month=today.month)[:20]
        context['images'] = Image.objects.order_by('-created_date').filter(gallery__isnull=True).filter(news__isnull=True).filter(docs__isnull=True)[:10]
        context['videos'] = Video.objects.order_by('-created_date')[:20]
        context['gallerys'] = Gallery.objects.order_by('-created_date')[:10]
        return context


# Create your views here.
# Vista basica para noticias
class NewsDefaultView(MenuMixin, DateDetailView):
    template_name = 'news_template.html'
    context_object_name = 'news'
    date_field = 'created_date'
    model = New
    month_format = '%m'

    def get(self, request, *args, **kwargs):
        a = self.get_object()
        if not request.session.get(str(a.id)):
            a.times_viewed += 1
            a.save()
            request.session[a.id] = True

        return super(NewsDefaultView, self).get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        week = week_range(today)
        context = super(NewsDefaultView, self).get_context_data(**kwargs)
        # Noticias recomendadas
        context['rnews'] = self.model.objects.order_by('-times_viewed').filter(is_published=True)[:3]
        # Ultimas noticias de la Semana
        context['wnews'] = self.model.objects.filter(created_date__range=week).filter(is_published=True)[:5]
        return context


# Vista de Pagina Principal
class NewsIndexView(MenuMixin, ListView):
    template_name = 'index.html'
    model = New

    # def get(self, request, *args, **kwargs):
    #    a = self.get_queryset()
    #    if not request.session.get(str(a.id)):
    #        return a

    def get_context_data(self, **kwargs):
        context = super(NewsIndexView, self).get_context_data(**kwargs)
        context['first_new'] = self.model.objects.filter(is_published=True).first()   # Ultima Noticia
        context['opinion'] = self.model.objects.filter(subtopic__name='Opinion').filter(is_published=True)[:3]
        context['tvideo'] = Video.objects.first()  # Video del dia
        context['cimage'] = Image.objects.filter(gallery__name='Caricaturas').order_by('-created_date')[:10]
        context['imnews'] = self.model.objects.filter(is_published=True)[:10]
        context['snews'] = \
            self.model.objects.filter(topic__slug='deportes').filter(is_published=True).order_by('-created_date')[:5]
        context['cnews'] = \
            self.model.objects.filter(topic__slug='cultura').filter(is_published=True).order_by('-created_date')[:5]
        context['pnews'] = \
            self.model.objects.filter(topic__slug='politica').filter(is_published=True).order_by('-created_date')[:5]
        context['dnews'] = \
            self.model.objects.filter(topic__slug='economia').filter(is_published=True).order_by('-created_date')[:5]
        context['psnews'] = \
            self.model.objects.filter(topic__slug='sociedad').filter(is_published=True).order_by('-created_date')[:5]
        context['tsnews'] = \
            self.model.objects.filter(subtopic__slug='turismo').filter(is_published=True).order_by('-created_date')[:5]
        return context

    def get_queryset(self):
        # today = datetime.date.today()
        # Para que no ponga muchas, máximo de 20 a 30
        # self.model.objects.order_by('-times_viewed').filter(created_date__year=today.year).
        # filter(created_date__month=today.month).filter(is_published=True)     #Diez noticias mas vistas del Mes
        return self.model.objects.filter(is_published=True)[10:16]


# Vista noticias de HOY
class TodayNewsView(MenuMixin, ListView):
    template_name = 'today_news.html'
    model = New
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(TodayNewsView, self).get_context_data(**kwargs)
        context['rnews'] = self.model.objects.order_by('-times_viewed').filter(is_published=True)[:3]  # Recomendadas
        context['lnews'] = self.model.objects.filter(is_published=True).all()[:5]    # Mas noticias
        context['mnews'] = self.model.objects.order_by('topic').filter(is_published=True)[:10]
        return context

    def get_queryset(self):
        today = datetime.date.today()
        return self.model.objects.filter(is_published=True).filter(created_date__year=today.year).filter(created_date__month=today.month).filter(created_date__day=today.day)


class NewsViewsOther(ListView):
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by',  self.paginate_by)

    def get_queryset(self):
        return New.objects.filter(is_published=True)

sort_by = {
    'd': '-created_date',
    't': 'title',
    'v': '-times_viewed',
}


class SearchNewsView(FacetedSearchView):
    template = 'search/search.html'

    def extra_context(self):
        # today = datetime.date.today()
        extra = super(SearchNewsView, self).extra_context()
        extra['lnews'] = New.objects.filter(is_published=True).all()[:10]    # Mas noticias
        return extra

    # def get_query(self):
        # searchqueryset = super(SearchNewsView, self).get_results()
        # searchqueryset = searchqueryset.models(New)

        # sort = self.request.GET.get('sort')
        # if sort in sort_by.keys():
        #    searchqueryset = searchqueryset.order_by('%s' % sort_by[sort])
        #    print(New.objects.filter().order_by('%s' % sort_by[sort]))
        #    return New.objects.filter().order_by('%s' % sort_by[sort])
        # else:
        #   searchqueryset = searchqueryset.order_by('-created_date')
        #    return New.objects.filter().order_by('-creation')

        # return searchqueryset