# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table('authors_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
            ('biography', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('link_own', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200)),
        ))
        db.send_create_signal('authors', ['Author'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table('authors_author')


    models = {
        'authors.author': {
            'Meta': {'ordering': "['last_name']", 'object_name': 'Author'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'link_own': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['authors']