import datetime
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.syndication.views import Feed
from django.contrib.sitemaps.views import sitemap, index

from news.views import NewsIndexView, SearchNewsView
from news.feeds import RssNewsFeed, AtomNewsFeed
from tiempoturco.sitemaps import *

from django.contrib import admin
from haystack.forms import SearchForm, FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import search_view_factory
from news.forms import CustomFacetedSearchForm


admin.autodiscover()

sitemaps = {
    "authors": AuthorsSitemap,
    "gallery": GallerysSitemap,
    "images": ImagesSitemap,
    "keywords": KeywordsSitemap,
    "news": NewsSitemap,
    "subtopic": SubtopicSitemap,
    "topic": TopicSitemap,
    "videos": VideosSitemap,
}

urlpatterns = patterns('',  # url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^i18n/', include('django.conf.urls.i18n')),
                       url(r'^admin/', include(admin.site.urls)),

    url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='admin_password_reset'),
    url(r'^admin/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    # Here own urls for module
    url(r'^authors/', include('authors.urls')),
    url(r'^visuals/', include('visuals.urls')),
    url(r'^docs/', include('docs.urls')),
    url(r'^tags/', include('tags.urls')),
    url(r'^news/', include('news.urls')),

    url(r'^rss/$', RssNewsFeed(), name="RssNewsFeed"),
    # url(r'^(?P<topic_name>[\w\-]+)/rss/$', RssNewsFeed(), name="RssNewsFeed"),

    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^robots\.txt$', include('robots.urls')),

    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.index', {'sitemaps': sitemaps}),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.index', {'sitemaps': sitemaps}),
    # url(r'^registerUser/', 'userProfiles.views.signUp',name='signUp'),
    # url(r'^loginUser/', 'userProfiles.views.loginUser',name='logIn'),

    url(r'^$', NewsIndexView.as_view(), name='index'),  # Index
)

urlpatterns += patterns(
    '',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, }),
)

# Haystack
today = datetime.date.today()
sqs = SearchQuerySet().facet('place').facet('author').date_facet('created_date', start_date=datetime.date(2014, 4, 20),
                                                                 end_date=today, gap_by='day', gap_amount=7)
urlpatterns += patterns('haystack.views',
    url(r'^search/', search_view_factory(
        view_class=SearchNewsView,
        searchqueryset=sqs,
        form_class=CustomFacetedSearchForm
    ), name='haystack_search'),
)
