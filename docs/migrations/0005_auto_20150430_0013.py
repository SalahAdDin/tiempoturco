# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0004_auto_20141005_1653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentation',
            options={'verbose_name': 'Documentation', 'verbose_name_plural': 'Documents', 'ordering': ('index',)},
        ),
        migrations.AlterField(
            model_name='documentation',
            name='author',
            field=models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL, related_name='docs'),
        ),
        migrations.AlterField(
            model_name='documentation',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='documentation',
            name='created_date',
            field=models.DateTimeField(verbose_name='Datetime', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='documentation',
            name='index',
            field=models.DecimalField(max_digits=4, unique=True, default=0, verbose_name='Index', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='documentation',
            name='title',
            field=models.CharField(unique=True, verbose_name='Title', max_length=255),
        ),
    ]
