# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.template.defaultfilters import slugify


class Migration(migrations.Migration):

    def slugify_fields(apps, schema_editor):
        KeyWord = apps.get_model("tags", "KeyWord")
        Topic = apps.get_model("tags", "Topic")
        Subtopic = apps.get_model("tags", "Subtopic")
        for keyword in KeyWord.objects.all():
            keyword.slug = slugify(keyword.name)
            keyword.save()
        for topic in Topic.objects.all():
            topic.slug = slugify(topic.name)
            topic.save()
        for subtopic in Subtopic.objects.all():
            subtopic.slug = slugify(subtopic.name)
            subtopic.save()

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='keyword',
            options={'verbose_name': 'Keyword', 'verbose_name_plural': 'Keywords', 'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='keyword',
            name='slug',
            field=models.SlugField(verbose_name='Slug', null=True, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='subtopic',
            name='slug',
            field=models.SlugField(verbose_name='Slug', null=True, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(verbose_name='Slug', null=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='name',
            field=models.CharField(verbose_name='Name', max_length=50, unique=True),
        ),
        migrations.RunPython(slugify_fields)
    ]
