# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'AttachedMedia'
        db.delete_table('media_attachedmedia')

        # Adding model 'AttachedMediaItem'
        db.create_table('media_attachedmediaitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('mediaset', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['media.MediaSet'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('media', ['AttachedMediaItem'])


    def backwards(self, orm):
        
        # Adding model 'AttachedMedia'
        db.create_table('media_attachedmedia', (
            ('object_id', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('mediaset', self.gf('django.db.models.fields.related.ForeignKey')(related_name='objects', to=orm['media.MediaSet'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('media', ['AttachedMedia'])

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
            'Meta': {'object_name': 'AttachedMediaItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediaset': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['media.MediaSet']"}),
            'object_id': ('django.db.models.fields.IntegerField', [], {}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'media.mediaset': {
            'Meta': {'unique_together': "(['content_type', 'object_id'],)", 'object_name': 'MediaSet'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['media']
