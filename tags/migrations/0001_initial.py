# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeyWord',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, verbose_name='Nombre', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Palabras Clave',
                'verbose_name': 'Palabra Clave',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Subtopic',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, verbose_name='Nombre', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Subtopics',
                'verbose_name': 'Subtopic',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, verbose_name='Nombre', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Topics',
                'verbose_name': 'Topic',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='subtopic',
            name='topic',
            field=models.ForeignKey(verbose_name='Topic', to='tags.Topic'),
        ),
    ]
