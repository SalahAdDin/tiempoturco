# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Gallery.created_date'
        db.add_column('gallery_gallery', 'created_date',
                      self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True, default=datetime.datetime(2014, 9, 6, 0, 0)),
                      keep_default=False)

        # Adding field 'Gallery.slug'
        db.add_column('gallery_gallery', 'slug',
                      self.gf('django.db.models.fields.SlugField')(unique=True, default=datetime.datetime(2014, 9, 6, 0, 0), max_length=100),
                      keep_default=False)

        # Adding field 'Gallery.times_viewed'
        db.add_column('gallery_gallery', 'times_viewed',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)


        # Changing field 'Gallery.author'
        db.alter_column('gallery_gallery', 'author_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    def backwards(self, orm):
        # Deleting field 'Gallery.created_date'
        db.delete_column('gallery_gallery', 'created_date')

        # Deleting field 'Gallery.slug'
        db.delete_column('gallery_gallery', 'slug')

        # Deleting field 'Gallery.times_viewed'
        db.delete_column('gallery_gallery', 'times_viewed')


        # Changing field 'Gallery.author'
        db.alter_column('gallery_gallery', 'author_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authors.Author']))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'gallery.gallery': {
            'Meta': {'object_name': 'Gallery', 'ordering': "['-name']"},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'news': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'null': 'True', 'blank': 'True', 'to': "orm['news.New']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'times_viewed': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'keywords.keyword': {
            'Meta': {'object_name': 'KeyWord', 'ordering': "['name']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'news.new': {
            'Meta': {'object_name': 'New', 'ordering': "['-created_date']"},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'news'", 'to': "orm['auth.User']"}),
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'news'", 'blank': 'True', 'to': "orm['keywords.KeyWord']"}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'source': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'}),
            'subtopic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'news'", 'to': "orm['subtopic.Subtopic']"}),
            'times_viewed': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'news'", 'to': "orm['topic.Topic']"})
        },
        'subtopic.subtopic': {
            'Meta': {'object_name': 'Subtopic', 'ordering': "['name']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['topic.Topic']"})
        },
        'topic.topic': {
            'Meta': {'object_name': 'Topic', 'ordering': "['name']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['gallery']