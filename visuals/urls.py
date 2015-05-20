from django.conf.urls import patterns, include, url

from .views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = \
    patterns('',
             url(r'^gallerys/(?P<slug>[\w\-]+)/$', GalleryDefaultView.as_view(), name='GalleryDefaultView'),
             url(r'^gallerys/', GalleryIndexView.as_view(), name='GalleryIndexView'),
             url(r'^images/(?P<slug>[\w\-]+)/$', ImageDefaultView.as_view(), name='ImageDefaultView'),
             url(r'^images/', ImageIndexView.as_view(), name='ImageIndexView'),
             url(r'^videos/(?P<slug>[\w\-]+)/$', VideoDefaultView.as_view(), name='VideoDefaultView'),
             url(r'^videos/', VideoIndexView.as_view(), name='VideoIndexView'),
             )