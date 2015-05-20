# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doc',
            options={'verbose_name': 'Documentacion', 'ordering': ['-created_date'], 'verbose_name_plural': 'Documentacion'},
        ),
        migrations.RemoveField(
            model_name='doc',
            name='is_published',
        ),
    ]
