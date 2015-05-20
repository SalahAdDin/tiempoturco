# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150421_0252'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'permissions': (('can_publish', 'Puede publicar noticias'),), 'verbose_name': 'New', 'verbose_name_plural': 'News', 'ordering': ('-created_date',)},
        ),
        migrations.AlterField(
            model_name='new',
            name='created_date',
            field=models.DateTimeField(verbose_name='Datetime', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='keywords',
            field=models.ManyToManyField(to='tags.KeyWord', verbose_name='Keywords', blank=True, related_name='news', help_text='Tags related with this new!'),
        ),
        migrations.AlterField(
            model_name='new',
            name='place',
            field=models.CharField(verbose_name='Place', max_length=255, help_text='Place in which the new happened. Normally is a city!'),
        ),
        migrations.AlterField(
            model_name='new',
            name='slug',
            field=models.SlugField(help_text="Put a title's copy as slug automatically!", unique=True, verbose_name='Slug', max_length=100),
        ),
        migrations.AlterField(
            model_name='new',
            name='source',
            field=models.URLField(verbose_name='Source', blank=True, help_text='Source of the new, for example, a web page.'),
        ),
        migrations.AlterField(
            model_name='new',
            name='times_viewed',
            field=models.PositiveIntegerField(editable=False, default=0, verbose_name='Times viewed'),
        ),
    ]
