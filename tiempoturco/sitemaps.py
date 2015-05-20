from django.contrib.sitemaps import Sitemap
from authors.models import AuthorInfo
from visuals.models import Gallery, Image, Video
from tags.models import KeyWord, Subtopic, Topic
from news.models import New


class NewsSitemap(Sitemap):
    changefreq = "always"
    priority = 0.8

    def items(self):
        # elementos del feed
        return New.objects.order_by('-created_date')

    def lastmod(self, obj):
        return obj.created_date


class AuthorsSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.6

    def items(self):
        # elementos del feed
        return AuthorInfo.objects.order_by('user')

    def lastmod(self, obj):
        return obj.user.last_login


class GallerysSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        # elementos del feed
        return Gallery.objects.order_by('-created_date')

    def lastmod(self, obj):
        return obj.created_date


class ImagesSitemap(Sitemap):
    changefreq = "always"
    priority = 0.6

    def items(self):
        # elementos del feed
        return Image.objects.order_by('-created_date')

    def lastmod(self, obj):
        return obj.created_date


class KeywordsSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.4

    def items(self):
        # elementos del feed
        return KeyWord.objects.order_by('slug')


class SubtopicSitemap(Sitemap):
    changefreq = "never"
    priority = 0.4

    def items(self):
        # elementos del feed
        return Subtopic.objects.order_by('slug')


class TopicSitemap(Sitemap):
    changefreq = "never"
    priority = 0.6

    def items(self):
        # elementos del feed
        return Topic.objects.order_by('slug')


class VideosSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        # elementos del feed
        return Video.objects.order_by('-created_date')

    def lastmod(self, obj):
        return obj.created_date