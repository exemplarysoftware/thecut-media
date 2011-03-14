# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'MediaSet', fields ['content_type', 'object_id']
        db.delete_unique('media_mediaset', ['content_type_id', 'object_id'])

        # Deleting model 'MediaSet'
        db.delete_table('media_mediaset')

        # Deleting field 'AttachedMediaItem.mediaset'
        db.delete_column('media_attachedmediaitem', 'mediaset_id')

        # Adding field 'AttachedMediaItem.parent_content_type'
        db.add_column('media_attachedmediaitem', 'parent_content_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='attachedmediaitem_parent_set', null=True, to=orm['contenttypes.ContentType']), keep_default=False)

        # Adding field 'AttachedMediaItem.parent_object_id'
        db.add_column('media_attachedmediaitem', 'parent_object_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'MediaSet'
        db.create_table('media_mediaset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('media', ['MediaSet'])

        # Adding unique constraint on 'MediaSet', fields ['content_type', 'object_id']
        db.create_unique('media_mediaset', ['content_type_id', 'object_id'])

        # We cannot add back in field 'AttachedMediaItem.mediaset'
        raise RuntimeError(
            "Cannot reverse this migration. 'AttachedMediaItem.mediaset' and its values cannot be restored.")

        # Deleting field 'AttachedMediaItem.parent_content_type'
        db.delete_column('media_attachedmediaitem', 'parent_content_type_id')

        # Deleting field 'AttachedMediaItem.parent_object_id'
        db.delete_column('media_attachedmediaitem', 'parent_object_id')


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
            'object_id': ('django.db.models.fields.IntegerField', [], {}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent_content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'attachedmediaitem_parent_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'parent_object_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['media']
