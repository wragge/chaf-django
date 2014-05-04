# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'lbs_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street_number_master', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('street_number_source', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('street_name_source', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('street_name_master', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('business_name', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('economic_activity', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'lbs', ['Location'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'lbs_location')


    models = {
        u'lbs.location': {
            'Meta': {'object_name': 'Location'},
            'business_name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'economic_activity': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'street_name_master': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'street_name_source': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'street_number_master': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'street_number_source': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lbs']