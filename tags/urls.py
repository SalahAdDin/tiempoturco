from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from .views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tiempoturco.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),

    #Lo ideal es que cada mòdulo tenga su propio archivo de direcciones url las cuàles solo afecten el mòdulo

    #url(r'^authors/(?P<first_name>[\w\-]+)/', 'authors.views.Author_view', name='Author.view'),
    url(r'^tags/(?P<slug>[\w\-]+)/$', KeyWordsNewsView.as_view(), name='KeyWordsNewsView'),
    url(r'^tags/', KeyWordsIndexView.as_view(), name='KeyWordsIndexView'), #Index
    url(r'^subtopic/(?P<slug>[\w\-]+)/$', SubTopicNewsView.as_view(), name='SubTopicNewsView'),
    url(r'^topic/(?P<slug>[\w\-]+)/$', TopicNewsView.as_view(), name='TopicNewsView'),
)