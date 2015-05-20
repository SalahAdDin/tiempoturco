from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from django.db import models


# Create your models here.
class KeyWord(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=50, unique=True,)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=100, unique=True, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Keyword')
        verbose_name_plural = _('Keywords')
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('KeyWordsNewsView', args=[str(self.slug)])

    def save(self):   # Definir metodo para guardar, validar y otros metodos del Slug
        super(KeyWord, self).save()  # Solo con este me funciona correctamente
        if not self.id:
            self.slug = slugify(self.title)
        super(KeyWord, self).save()


class Topic(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255, unique=True, )
    slug = models.SlugField(verbose_name=_('Slug'), max_length=100, unique=True, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('TopicNewsView', args=[str(self.slug)])

    def save(self):  # Definir metodo para guardar, validar y otros metodos del Slug
        super(Topic, self).save()  # Solo con este me funciona correctamente
        if not self.id:
            self.slug = slugify(self.title)
        super(Topic, self).save()


class Subtopic(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255, )
    slug = models.SlugField(verbose_name=_('Slug'), max_length=100, unique=True, )
    topic = models.ForeignKey(Topic, verbose_name=_('Topic'), related_name='subs', )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Subtopic')
        verbose_name_plural = _('Subtopics')
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('SubTopicNewsView', args=[str(self.slug)])

    def save(self):  # Definir metodo para guardar, validar y otros metodos del Slug
        super(Subtopic, self).save()  # Solo con este me funciona correctamente
        if not self.id:
            self.slug = slugify(self.title)
        super(Subtopic, self).save()