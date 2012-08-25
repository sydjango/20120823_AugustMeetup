# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.password'
        db.delete_column('southintro_user', 'password')


    def backwards(self, orm):
        # Adding field 'User.password'
        db.add_column('southintro_user', 'password',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60),
                      keep_default=False)


    models = {
        'southintro.user': {
            'Meta': {'object_name': 'User'},
            'haircolour': ('django.db.models.fields.CharField', [], {'default': "'OTHR'", 'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'password_hash': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'password_salt': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['southintro']