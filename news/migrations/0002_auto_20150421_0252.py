# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='subtopic',
            field=smart_selects.db_fields.ChainedForeignKey(verbose_name='Subtopic', related_name='news', to='tags.Subtopic'),
        ),
    ]
