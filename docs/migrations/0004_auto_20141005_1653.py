# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0003_auto_20140915_1930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentation',
            options={'verbose_name': 'Documentación', 'ordering': ['index'], 'verbose_name_plural': 'Documentación'},
        ),
        migrations.AddField(
            model_name='documentation',
            name='index',
            field=models.DecimalField(unique=True, max_digits=4, verbose_name='Indice', default=0, decimal_places=2),
            preserve_default=True,
        ),
    ]
