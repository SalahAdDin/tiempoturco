# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('created_date', models.DateTimeField(verbose_name='Date and Hour', auto_now_add=True)),
                ('is_published', models.BooleanField(verbose_name='Published', default=False)),
                ('place', models.CharField(verbose_name='Place', max_length=255)),
                ('source', models.URLField(verbose_name='Source', blank=True)),
                ('times_viewed', models.PositiveIntegerField(editable=False, verbose_name='Times Viewed', default=0)),
                ('title', models.CharField(verbose_name='Title', unique=True, max_length=255)),
                ('slug', models.SlugField(verbose_name='Slug', unique=True, max_length=100)),
                ('author', models.ForeignKey(verbose_name='Author', related_name='news', to=settings.AUTH_USER_MODEL)),
                ('keywords', models.ManyToManyField(verbose_name='Keywords', blank=True, related_name='news', to='tags.KeyWord')),
                ('subtopic', models.ForeignKey(verbose_name='Subtopic', related_name='news', to='tags.Subtopic')),
                ('topic', models.ForeignKey(verbose_name='Topic', related_name='news', to='tags.Topic')),
            ],
            options={
                'verbose_name_plural': 'news',
                'verbose_name': 'new',
                'permissions': (('can_publish', 'Puede publicar noticias'),),
                'ordering': ('-created_date',),
            },
        ),
    ]
