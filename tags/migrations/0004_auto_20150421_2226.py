# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_auto_20150421_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopic',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='topic',
            field=models.ForeignKey(related_name='subs', to='tags.Topic', verbose_name='Topic'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Name'),
        ),
    ]
