# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Remember to use orm['appname.ModelName'] rather than "from appname.models.
        import random, hashlib, string
        for user in orm.User.objects.all():
            user.password_salt = "".join([random.choice(string.letters) for i in range(8)])
            user.password_hash = hashlib.sha256(user.password_salt + user.password).hexdigest()
            user.save()

    def backwards(self, orm):
        "Write your backwards methods here."
        raise RuntimeError("Cannot reverse this migration.")

    models = {
        'southintro.user': {
            'Meta': {'object_name': 'User'},
            'haircolour': ('django.db.models.fields.CharField', [], {'default': "'OTHR'", 'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'password_hash': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'password_salt': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['southintro']
    symmetrical = True
