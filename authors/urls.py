from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin


from django.contrib import admin
from .views import *

admin.autodiscover()

urlpatterns = \
    patterns('',
             # url(r'^(?P<first_name>[\w\-]+)/', 'authors.views.Author_view', name='Author.view'),
             url(r'^(?P<username>[\w\-]+)/$', AuthorInfoView.as_view(), name='AuthorInfoView'),
             url(r'^', AuthorInfoIndexView.as_view(), name='AuthorInfoIndexView'),  # Index
             )