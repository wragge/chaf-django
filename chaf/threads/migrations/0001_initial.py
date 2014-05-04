# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MarriageRegistration'
        db.create_table(u'threads_marriageregistration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reg_number', self.gf('django.db.models.fields.IntegerField')()),
            ('reg_year', self.gf('django.db.models.fields.IntegerField')()),
            ('index_spouse1_surname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('index_spouse1_firstname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('index_spouse2_surname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('index_spouse2_firstname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('index_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('index_registration_place', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('marriage_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('marriage_place', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('marriage_church', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('celebrant_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('witnesses', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('husband_surname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('husband_firstname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('husband_occupation', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('husband_residence', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('husband_status', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('husband_birthplace', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('husband_birthdate', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('husband_age', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('husband_father_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('husband_father_occupation', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('husband_mother_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('husband_mother_maiden_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('husband_mother_occupation', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('wife_surname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('wife_firstname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('wife_occupation', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('wife_residence', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('wife_status', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('wife_birthplace', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('wife_birthdate', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('wife_age', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('wife_father_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('wife_father_occupation', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('wife_mother_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('wife_mother_maiden_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('wife_mother_occupation', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'threads', ['MarriageRegistration'])

        # Adding model 'BirthRegistration'
        db.create_table(u'threads_birthregistration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reg_number', self.gf('django.db.models.fields.IntegerField')()),
            ('reg_year', self.gf('django.db.models.fields.IntegerField')()),
            ('index_child_firstname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('index_child_surname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('index_father_firstname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('index_mother_firstname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('index_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('index_registration_place', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('child_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('child_sex', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('birthdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('birthplace', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('informant_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('witnesses', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('father_surname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('father_firstname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('father_occupation', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('father_birthplace', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('father_age', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('mother_surname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('mother_firstname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('mother_maiden_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('mother_occupation', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('mother_birthplace', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('mother_age', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('marriage_date', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('previous_children', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'threads', ['BirthRegistration'])


    def backwards(self, orm):
        # Deleting model 'MarriageRegistration'
        db.delete_table(u'threads_marriageregistration')

        # Deleting model 'BirthRegistration'
        db.delete_table(u'threads_birthregistration')


    models = {
        u'threads.birthregistration': {
            'Meta': {'object_name': 'BirthRegistration'},
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'birthplace': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'child_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'child_sex': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'father_age': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'father_birthplace': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'father_firstname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'father_occupation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'father_surname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_child_firstname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'index_child_surname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'index_father_firstname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'index_mother_firstname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'index_registration_place': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'index_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'informant_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'marriage_date': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mother_age': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mother_birthplace': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'mother_firstname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mother_maiden_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mother_occupation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'mother_surname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'previous_children': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'reg_number': ('django.db.models.fields.IntegerField', [], {}),
            'reg_year': ('django.db.models.fields.IntegerField', [], {}),
            'witnesses': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'threads.marriageregistration': {
            'Meta': {'object_name': 'MarriageRegistration'},
            'celebrant_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'husband_age': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'husband_birthdate': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'husband_birthplace': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'husband_father_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'husband_father_occupation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'husband_firstname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'husband_mother_maiden_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'husband_mother_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'husband_mother_occupation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'husband_occupation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'husband_residence': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'husband_status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'husband_surname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_registration_place': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'index_spouse1_firstname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'index_spouse1_surname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'index_spouse2_firstname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'index_spouse2_surname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'index_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'marriage_church': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'marriage_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'marriage_place': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'reg_number': ('django.db.models.fields.IntegerField', [], {}),
            'reg_year': ('django.db.models.fields.IntegerField', [], {}),
            'wife_age': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'wife_birthdate': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'wife_birthplace': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'wife_father_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'wife_father_occupation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'wife_firstname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'wife_mother_maiden_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'wife_mother_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'wife_mother_occupation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'wife_occupation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'wife_residence': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'wife_status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'wife_surname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'witnesses': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['threads']