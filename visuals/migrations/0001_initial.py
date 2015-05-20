# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gallery'
        db.create_table('gallery_gallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authors.Author'])),
            ('news', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, null=True, unique=True, to=orm['news.New'])),
        ))
        db.send_create_signal('gallery', ['Gallery'])


    def backwards(self, orm):
        # Deleting model 'Gallery'
        db.delete_table('gallery_gallery')


    models = {
        'authors.author': {
            'Meta': {'object_name': 'Author', 'ordering': "['last_name']"},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'link_own': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'})
        },
        'gallery.gallery': {
            'Meta': {'object_name': 'Gallery', 'ordering': "['-name']"},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authors.Author']"}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'news': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'null': 'True', 'unique': 'True', 'to': "orm['news.New']"})
        },
        'keywords.keyword': {
            'Meta': {'object_name': 'KeyWord', 'ordering': "['name']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'news.new': {
            'Meta': {'object_name': 'New', 'ordering': "['-created_date']"},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authors.Author']", 'related_name': "'news'"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['keywords.KeyWord']", 'symmetrical': 'False', 'related_name': "'news'"}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'source': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'}),
            'subtopic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['subtopic.Subtopic']", 'related_name': "'news'"}),
            'times_viewed': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['topic.Topic']", 'related_name': "'news'"})
        },
        'subtopic.subtopic': {
            'Meta': {'object_name': 'Subtopic', 'ordering': "['name']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['topic.Topic']"})
        },
        'topic.topic': {
            'Meta': {'object_name': 'Topic', 'ordering': "['name']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'})
        }
    }

    complete_apps = ['gallery']