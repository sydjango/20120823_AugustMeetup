# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('southintro_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('southintro', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table('southintro_user')


    models = {
        'southintro.user': {
            'Meta': {'object_name': 'User'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['southintro']