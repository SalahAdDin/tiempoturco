from django.contrib.syndication.views import Feed
from django.contrib.syndication.views import FeedDoesNotExist
from django.shortcuts import get_object_or_404
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed
from .models import New
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden


class MediaRSSFeed(Rss201rev2Feed):
    """Basic implementation of Yahoo Media RSS (mrss)
    http://video.search.yahoo.com/mrss

    Includes these elements in the Item feed:
    media:content
        url, width, height
    media:thumbnail
        url, width, height
    media:description
    media:title
    media:keywords
    """
    def rss_attributes(self):
        attrs = super(MediaRSSFeed, self).rss_attributes()
        attrs['xmlns:media'] = 'http://search.yahoo.com/mrss/'
        attrs['xmlns:atom'] = 'http://www.w3.org/2005/Atom'
        return attrs

    def add_item_elements(self, handler, item):
        """Callback to add elements to each item (item/entry) element."""
        super(MediaRSSFeed, self).add_item_elements(handler, item)

        if 'media:title' in item:
            handler.addQuickElement(u"media:title", item['title'])
        if 'media:description' in item:
            handler.addQuickElement(u"media:description", item['description'])

        if 'content_url' in item:
            content = dict(url=item['content_url'])
            if 'content_width' in item:
                content['width'] = str(item['content_width'])
            if 'content_height' in item:
                content['height'] = str(item['content_height'])
            handler.addQuickElement(u"media:content", '', content)

        if 'thumbnail_url' in item:
            thumbnail = dict(url=item['thumbnail_url'])
            if 'thumbnail_width' in item:
                thumbnail['width'] = str(item['thumbnail_width'])
            if 'thumbnail_height' in item:
                thumbnail['height'] = str(item['thumbnail_height'])
            handler.addQuickElement(u"media:thumbnail", '', thumbnail)

        if 'keywords' in item:
            handler.addQuickElement(u"media:keywords", item['keywords'])


class RssNewsFeed(Feed):
    author_name = 'Tiempo Turco'
    categories = ("Noticias", "Turquía")
    description = 'Portal de Noticias de Turquía en Español para Latino América, para el mundo de habla Hispana.' \
                  ' Manténgase de lo que pasa en Turquía, ahora en su idioma.'
    feed_copyright = 'Copyright (c) 2014, Tiempo Turco. Desarrollado por Barakat Studios'
    feed_guid = '/rss/2014'
    feed_type = MediaRSSFeed
    feed_url = '/rss/'
    link = '/news/'
    title = 'Tiempo Turco Noticias'

    def items(self):
        # elementos del feed
        return New.objects.order_by('-created_date')

    def item_link(self, item):
        # Enlace a la noticia
        return reverse('NewsDefaultView',
                       args=[str(item.created_date.strftime("%Y")), str(item.created_date.strftime("%m")),
                             str(item.created_date.strftime("%d")), str(item.slug)])

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_created_date(self, item):
        # Fecha de creacion de la noticia en el feed
        return item.created_date

    def item_author_name(self, item):
        # nombre del autor de cada elemento del feed
        return item.author.get_full_name()

    def item_extra_kwargs(self, New):
        """Return a dictionary to the feedgenerator for each item to be added to the feed.
        If the object is a Gallery, uses a random sample image for use as the feed Item
        """
        photo = New.first_image()

        item = {'media:title': photo.name,
                'media:description': photo.caption,
                'content_url': photo.image, }

        # if len(item.keywords) > 0:
        keywords = New.get_all_keys()  # ','.join(item.keywords.split())
        item['keywords'] = keywords

        return item


class AtomNewsCustomFeed(Atom1Feed):
    """Custom Atom feed generator.
    This class will form the structure of the custom RSS feed.
    It's used to add a new tag element to each of the 'item's.
    """
    def add_item_elements(self, handler, item):
        # Invoke this same method of the super-class to add the standard elements to the 'item's.
        super(AtomNewsCustomFeed, self).add_item_elements(handler, item)
        # Add a new custom element named 'content' to each of the tag 'item'.
        handler.addQuickElement(u"Contenido", item['content'])


class AtomNewsFeed(RssNewsFeed):
    """Class used to generate the final customized Atom feed.
    Since this is a subclass of the RSS feed class it'll inherit its methods.
    """
    feed_type = AtomNewsCustomFeed		# Custom Atom feed.
    subtitle = RssNewsFeed.description		# Use the description of the RSS feed for this root tag.

    def __call__(self, request, *args, **kwargs):
        """Place for intercepting the call to the custom Atom feed, and perform
        pre-processing checks.
        """
        # Only authenticated users can view the feed.
        if not request.user.is_authenticated():
            return HttpResponseForbidden("<h3>Access Forbidden. User must be authenticated to access page.</h3>")
        else:
            return super(AtomNewsFeed, self).__call__(request, *args, **kwargs)

    def item_extra_kwargs(self, item):
        """
        Returns an extra keyword arguments dictionary that is used with
        the `add_item` call of the feed generator.
        Add the 'content' field of the 'Entry' item, to be used by the custom feed generator.
        """
        return {'content': item.content, }