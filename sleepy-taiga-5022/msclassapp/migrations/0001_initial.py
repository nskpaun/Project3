# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Scripture'
        db.create_table('msclassapp_scripture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('badge_url', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('reference', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('view_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('msclassapp', ['Scripture'])

        # Adding model 'Question'
        db.create_table('msclassapp_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scripture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['msclassapp.Scripture'])),
            ('question_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('msclassapp', ['Question'])

        # Adding model 'Trait'
        db.create_table('msclassapp_trait', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scripture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['msclassapp.Scripture'])),
            ('trait', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('msclassapp', ['Trait'])


    def backwards(self, orm):
        # Deleting model 'Scripture'
        db.delete_table('msclassapp_scripture')

        # Deleting model 'Question'
        db.delete_table('msclassapp_question')

        # Deleting model 'Trait'
        db.delete_table('msclassapp_trait')


    models = {
        'msclassapp.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'scripture': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['msclassapp.Scripture']"})
        },
        'msclassapp.scripture': {
            'Meta': {'object_name': 'Scripture'},
            'badge_url': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'view_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'msclassapp.trait': {
            'Meta': {'object_name': 'Trait'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scripture': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['msclassapp.Scripture']"}),
            'trait': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['msclassapp']