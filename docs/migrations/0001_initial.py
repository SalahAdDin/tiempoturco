# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora')),
                ('is_published', models.BooleanField(verbose_name='Publicada', default=False)),
                ('times_viewed', models.PositiveIntegerField(editable=False, verbose_name='Veces Vista', default=0)),
                ('title', models.CharField(max_length=255, verbose_name='Título', unique=True)),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug', unique=True)),
                ('author', models.ForeignKey(related_name='docs', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
