# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AttachedMediaItem'
        db.create_table('media_attachedmediaitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')()),
            ('parent_content_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='attachedmediaitem_parent_set', null=True, to=orm['contenttypes.ContentType'])),
            ('parent_object_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('media', ['AttachedMediaItem'])


    def backwards(self, orm):
        
        # Deleting model 'AttachedMediaItem'
        db.delete_table('media_attachedmediaitem')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'media.attachedmediaitem': {
            'Meta': {'ordering': "['order']", 'object_name': 'AttachedMediaItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent_content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'attachedmediaitem_parent_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'parent_object_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['media']
