# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20150421_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='Slug', unique=True),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='Slug', unique=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='Slug', unique=True),
        ),
    ]
