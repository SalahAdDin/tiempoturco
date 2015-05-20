from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField

# Create your models here.


class Documentation(models.Model):
    author = models.ForeignKey(User, verbose_name=_('Author'), related_name='docs',)
    content = RichTextField(verbose_name=_('Content'), )
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Datetime'), )
    index = models.DecimalField(default=0, max_digits=4, decimal_places=2, verbose_name=_('Index'), unique=True)
    title = models.CharField(verbose_name=_('Title'), max_length=255, unique=True,)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=100, unique=True,)

    class Meta:
        verbose_name_plural = _('Documents')
        verbose_name = _('Documentation')
        ordering = ('index', )

    def get_absolute_url(self):
        return reverse('DocsDefaultView', args=[str(self.slug)])

    def get_all_images(self):
        return self.images.all()

    def get_all_videos(self):
        return self.videos.all()