from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail import ImageField
from embed_video.fields import EmbedVideoField

from news.models import New
from docs.models import Documentation


# Create your models here.
class Gallery (models.Model):
    author = models.ForeignKey(User, verbose_name=_('Author'))
    caption = models.CharField(verbose_name=_('Description'), max_length=255,
                               help_text=_('Brief description of this gallery.'), )
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Datetime'))
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    news = models.OneToOneField(New, verbose_name=_('New'), blank=True, null=True,
                                help_text=_('New related with this Gallery.'), )
    slug = models.SlugField(verbose_name=_('Slug'), max_length=100, unique=True,
                            help_text=_("Put a title's copy as slug automatically. "
                                        "Please, put a appropriate name for this Gallery!"), )
    times_viewed = models.PositiveIntegerField(default=0, editable=False, verbose_name=_('Times viewed'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('GalleryDefaultView', args=[str(self.slug)])

    def get_all_images(self):
        return self.images.all()

    def get_image_count(self):
        return self.images.all().count()

    def get_first_image(self):
        return self.images.first()

    def get_all_videos(self):
        return self.videos.all()

    def get_video_count(self):
        return self.videos.all().count()

    def get_first_video(self):
        return self.videos.first()

    def save(self):   # Definir metodo para guardar, validar y otros metodos del Slug
        super(Gallery, self).save()  # Solo con este me funciona correctamente
        if not self.id:
            self.slug = slugify(self.title)
        super(Gallery, self).save()

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')
        ordering = ('name',)


class Image(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255, )
    image = ImageField(verbose_name=_('Image'), upload_to='images/news', )
    caption = models.CharField(verbose_name=_('Description'), max_length=355,
                               help_text=_("Brief description of this image, for example, in a news webpage, "
                                           "the text under new's image.(Copy it and put here.)"), )
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Datetime'), )
    docs = \
        models.ForeignKey(Documentation, verbose_name=_('Documentation'), null=True, blank=True, related_name='images',
                          help_text=_('Document related with this Image.'), )
    gallery = models.ForeignKey(Gallery, verbose_name=_('Gallery'), blank=True, null=True, related_name='images',
                                help_text=_('Gallery related with this Image.'), )
    news = models.ForeignKey(New, verbose_name=_('New'), blank=True, null=True, related_name='images',
                             help_text=_('New related with this Image.'), )
    slug = models.SlugField(verbose_name=_('Slug'), max_length=100, unique=True,
                            help_text=_("Put a title's copy as slug automatically. "
                                        "Please, put a appropriate name for this Image!"), )
    times_viewed = models.PositiveIntegerField(default=0, editable=False, verbose_name=_('Times viewed'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ImageDefaultView', args=[str(self.slug)])

    def save(self):   # Definir metodo para guardar, validar y otros metodos del Slug
        super(Image, self).save()  # Solo con este me funciona correctamente
        if not self.id:
            self.slug = slugify(self.title)
        super(Image, self).save()

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        ordering = ('-news__title',)


class Video(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255, )
    caption = models.CharField(verbose_name=_('Description'), max_length=255,
                               help_text=_('Brief description about this video.'), )
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Datetime'),)
    docs = \
        models.ForeignKey(Documentation, verbose_name=_('Documentation'), null=True, blank=True, related_name='videos',
                          help_text=_('Document related with this Video.'), )
    gallery = models.ForeignKey(Gallery, verbose_name=_('Gallery'), null=True, blank=True, related_name='videos',
                                help_text=_('Gallery related with this Video.'), )
    news = models.OneToOneField(New, verbose_name=_('New'), null=True, blank=True, related_name='videos',
                                help_text=_('New related with this Video.'), )
    times_viewed = models.PositiveIntegerField(default=0, editable=False, verbose_name=_('Times viewed'),)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=100, unique=True,
                            help_text=_("Put a title's copy as slug automatically. "
                                        "Please, put a appropriate name for this Video!"), )
    video = EmbedVideoField(verbose_name=_('Video'), help_text=_("Video's URL, for example, youtube's url."),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('VideoDefaultView', args=[str(self.slug)])

    def save(self):   # Definir metodo para guardar, validar y otros metodos del Slug
        super(Video, self).save()  # Solo con este me funciona correctamente
        if not self.id:
            self.slug = slugify(self.title)
        super(Video, self).save()

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')
        ordering = ('-name',)