# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('docs', '0002_auto_20140913_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora')),
                ('title', models.CharField(unique=True, max_length=255, verbose_name='Título')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='Slug')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='docs', verbose_name='Autor')),
            ],
            options={
                'ordering': ['-created_date'],
                'verbose_name': 'Documentación',
                'verbose_name_plural': 'Documentación',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='doc',
            name='author',
        ),
        migrations.DeleteModel(
            name='Doc',
        ),
    ]