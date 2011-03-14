# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Video'
        db.delete_table('media_video')

        # Removing M2M table for field sites on 'Video'
        db.delete_table('media_video_sites')

        # Deleting model 'Gallery'
        db.delete_table('media_gallery')

        # Removing M2M table for field images on 'Gallery'
        db.delete_table('media_gallery_images')

        # Removing M2M table for field sites on 'Gallery'
        db.delete_table('media_gallery_sites')

        # Deleting model 'Document'
        db.delete_table('media_document')

        # Adding model 'AttachedMedia'
        db.create_table('media_attachedmedia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('mediaset', self.gf('django.db.models.fields.related.ForeignKey')(related_name='objects', to=orm['media.MediaSet'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('media', ['AttachedMedia'])

        # Deleting field 'MediaSet.image_order'
        db.delete_column('media_mediaset', 'image_order')

        # Removing M2M table for field images on 'MediaSet'
        db.delete_table('media_mediaset_images')

        # Removing M2M table for field galleries on 'MediaSet'
        db.delete_table('media_mediaset_galleries')

        # Removing M2M table for field documents on 'MediaSet'
        db.delete_table('media_mediaset_documents')


    def backwards(self, orm):
        
        # Adding model 'Video'
        db.create_table('media_video', (
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('publish_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='video_publish_by_user', null=True, to=orm['auth.User'], blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='video_created_by_user', to=orm['auth.User'])),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('template', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='video_updated_by_user', to=orm['auth.User'])),
            ('tags', self.gf('tagging.fields.TagField')(null=True)),
            ('is_indexable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('publish_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, db_index=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('expire_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('media', ['Video'])

        # Adding M2M table for field sites on 'Video'
        db.create_table('media_video_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['media.video'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('media_video_sites', ['video_id', 'site_id'])

        # Adding model 'Gallery'
        db.create_table('media_gallery', (
            ('image_order', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=250, null=True, blank=True)),
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('publish_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='gallery_publish_by_user', null=True, to=orm['auth.User'], blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='gallery_created_by_user', to=orm['auth.User'])),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('template', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='gallery_updated_by_user', to=orm['auth.User'])),
            ('tags', self.gf('tagging.fields.TagField')(null=True)),
            ('is_indexable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('publish_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, db_index=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('expire_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('media', ['Gallery'])

        # Adding M2M table for field images on 'Gallery'
        db.create_table('media_gallery_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gallery', models.ForeignKey(orm['media.gallery'], null=False)),
            ('photo', models.ForeignKey(orm['photologue.photo'], null=False))
        ))
        db.create_unique('media_gallery_images', ['gallery_id', 'photo_id'])

        # Adding M2M table for field sites on 'Gallery'
        db.create_table('media_gallery_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gallery', models.ForeignKey(orm['media.gallery'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('media_gallery_sites', ['gallery_id', 'site_id'])

        # Adding model 'Document'
        db.create_table('media_document', (
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='document_updated_by_user', to=orm['auth.User'])),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('publish_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('publish_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='document_publish_by_user', null=True, to=orm['auth.User'], blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='document_created_by_user', to=orm['auth.User'])),
            ('expire_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('media', ['Document'])

        # Deleting model 'AttachedMedia'
        db.delete_table('media_attachedmedia')

        # Adding field 'MediaSet.image_order'
        db.add_column('media_mediaset', 'image_order', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=250, null=True, blank=True), keep_default=False)

        # Adding M2M table for field images on 'MediaSet'
        db.create_table('media_mediaset_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mediaset', models.ForeignKey(orm['media.mediaset'], null=False)),
            ('photo', models.ForeignKey(orm['photologue.photo'], null=False))
        ))
        db.create_unique('media_mediaset_images', ['mediaset_id', 'photo_id'])

        # Adding M2M table for field galleries on 'MediaSet'
        db.create_table('media_mediaset_galleries', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mediaset', models.ForeignKey(orm['media.mediaset'], null=False)),
            ('gallery', models.ForeignKey(orm['media.gallery'], null=False))
        ))
        db.create_unique('media_mediaset_galleries', ['mediaset_id', 'gallery_id'])

        # Adding M2M table for field documents on 'MediaSet'
        db.create_table('media_mediaset_documents', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mediaset', models.ForeignKey(orm['media.mediaset'], null=False)),
            ('document', models.ForeignKey(orm['media.document'], null=False))
        ))
        db.create_unique('media_mediaset_documents', ['mediaset_id', 'document_id'])


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'media.attachedmedia': {
            'Meta': {'object_name': 'AttachedMedia'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediaset': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'objects'", 'to': "orm['media.MediaSet']"}),
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
