from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from datetime import datetime

from django.views.generic import DetailView
from .views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[\w\-]+)/$',
                           NewsDefaultView.as_view(), name='NewsDefaultView'),  # Noticia
                       url(r'^today/', TodayNewsView.as_view(), name='TodayNewsView')
                       # url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<slug>[\w\-]+)/',
                       # 'news.views.New_view', name='New.view'),
                       )