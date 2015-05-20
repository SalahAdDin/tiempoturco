import json
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from django.views.generic import ListView

from actions import week_range
import datetime

from news.models import New
from visuals.models import Gallery, Video, Image
from .models import AuthorInfo


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


# Vista basica para Author
class AuthorInfoView(MenuMixin, ListView):
    template_name = 'authors_template.html'
    paginate_by = 10
    model = New
    username_field = 'username'

    def get_context_data(self, **kwargs):
        author = self.kwargs.get('username')
        context = super(AuthorInfoView, self).get_context_data(**kwargs)
        context['users'] = User.objects.get(username__iexact=author)
        context['featured'] = \
            self.model.objects.order_by('-times_viewed').filter(author__username=author).filter(is_published=True)[:20]
        context['gallerys'] = Gallery.objects.order_by('-created_date').filter(author__username=author)[:20]
        return context

    def get_queryset(self):
        author = self.kwargs.get('username')
        return self.model.objects.filter(author__username=author).filter(is_published=True)


class AuthorInfoIndexView(MenuMixin, ListView):
    template_name = 'author_index_templates.html'
    paginate_by = 10
    model = AuthorInfo
