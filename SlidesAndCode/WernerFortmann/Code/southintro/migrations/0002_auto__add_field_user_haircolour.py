# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.haircolour'
        db.add_column('southintro_user', 'haircolour',
                      self.gf('django.db.models.fields.CharField')(default='OTHR', max_length=4),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.haircolour'
        db.delete_column('southintro_user', 'haircolour')


    models = {
        'southintro.user': {
            'Meta': {'object_name': 'User'},
            'haircolour': ('django.db.models.fields.CharField', [], {'default': "'OTHR'", 'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['southintro']