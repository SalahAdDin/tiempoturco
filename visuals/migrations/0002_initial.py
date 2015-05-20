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
            ('news', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['news.New'], blank=True, null=True, unique=True)),
        ))
        db.send_create_signal('gallery', ['Gallery'])


    def backwards(self, orm):
        # Deleting model 'Gallery'
        db.delete_table('gallery_gallery')


    models = {
        'authors.author': {
            'Meta': {'ordering': "['last_name']", 'object_name': 'Author'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'link_own': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'})
        },
        'gallery.gallery': {
            'Meta': {'ordering': "['-name']", 'object_name': 'Gallery'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authors.Author']"}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'news': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['news.New']", 'blank': 'True', 'null': 'True', 'unique': 'True'})
        },
        'keywords.keyword': {
            'Meta': {'ordering': "['name']", 'object_name': 'KeyWord'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'news.new': {
            'Meta': {'ordering': "['-created_date']", 'object_name': 'New'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authors.Author']", 'related_name': "'news'"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['keywords.KeyWord']", 'blank': 'True', 'related_name': "'news'", 'symmetrical': 'False'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'source': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'}),
            'subtopic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['subtopic.Subtopic']", 'related_name': "'news'"}),
            'times_viewed': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['topic.Topic']", 'related_name': "'news'"})
        },
        'subtopic.subtopic': {
            'Meta': {'ordering': "['name']", 'object_name': 'Subtopic'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['topic.Topic']"})
        },
        'topic.topic': {
            'Meta': {'ordering': "['name']", 'object_name': 'Topic'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['gallery']