# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'YoutubeVideo.tags'
        db.alter_column('mediasources_youtubevideo', 'tags', self.gf('tagging.fields.TagField')())

        # Changing field 'YoutubeVideo.content'
        db.alter_column('mediasources_youtubevideo', 'content', self.gf('django.db.models.fields.TextField')())

        # Changing field 'YoutubeVideo.caption'
        db.alter_column('mediasources_youtubevideo', 'caption', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Image.tags'
        db.alter_column('mediasources_image', 'tags', self.gf('tagging.fields.TagField')())

        # Changing field 'Image.content'
        db.alter_column('mediasources_image', 'content', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Image.caption'
        db.alter_column('mediasources_image', 'caption', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Video.tags'
        db.alter_column('mediasources_video', 'tags', self.gf('tagging.fields.TagField')())

        # Changing field 'Video.content'
        db.alter_column('mediasources_video', 'content', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Video.caption'
        db.alter_column('mediasources_video', 'caption', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Document.tags'
        db.alter_column('mediasources_document', 'tags', self.gf('tagging.fields.TagField')())

        # Changing field 'Document.content'
        db.alter_column('mediasources_document', 'content', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Document.caption'
        db.alter_column('mediasources_document', 'caption', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.tags'
        db.alter_column('mediasources_audio', 'tags', self.gf('tagging.fields.TagField')())

        # Changing field 'Audio.content'
        db.alter_column('mediasources_audio', 'content', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.caption'
        db.alter_column('mediasources_audio', 'caption', self.gf('django.db.models.fields.TextField')())

        # Changing field 'VimeoVideo._api_data'
        db.alter_column('mediasources_vimeovideo', '_api_data', self.gf('django.db.models.fields.TextField')())

        # Changing field 'VimeoVideo.tags'
        db.alter_column('mediasources_vimeovideo', 'tags', self.gf('tagging.fields.TagField')())

        # Changing field 'VimeoVideo.content'
        db.alter_column('mediasources_vimeovideo', 'content', self.gf('django.db.models.fields.TextField')())

        # Changing field 'VimeoVideo.caption'
        db.alter_column('mediasources_vimeovideo', 'caption', self.gf('django.db.models.fields.TextField')())

        # Changing field 'VimeoVideo._oembed_data'
        db.alter_column('mediasources_vimeovideo', '_oembed_data', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'YoutubeVideo.tags'
        db.alter_column('mediasources_youtubevideo', 'tags', self.gf('tagging.fields.TagField')(null=True))

        # Changing field 'YoutubeVideo.content'
        db.alter_column('mediasources_youtubevideo', 'content', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'YoutubeVideo.caption'
        db.alter_column('mediasources_youtubevideo', 'caption', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Image.tags'
        db.alter_column('mediasources_image', 'tags', self.gf('tagging.fields.TagField')(null=True))

        # Changing field 'Image.content'
        db.alter_column('mediasources_image', 'content', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Image.caption'
        db.alter_column('mediasources_image', 'caption', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Video.tags'
        db.alter_column('mediasources_video', 'tags', self.gf('tagging.fields.TagField')(null=True))

        # Changing field 'Video.content'
        db.alter_column('mediasources_video', 'content', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Video.caption'
        db.alter_column('mediasources_video', 'caption', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Document.tags'
        db.alter_column('mediasources_document', 'tags', self.gf('tagging.fields.TagField')(null=True))

        # Changing field 'Document.content'
        db.alter_column('mediasources_document', 'content', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Document.caption'
        db.alter_column('mediasources_document', 'caption', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Audio.tags'
        db.alter_column('mediasources_audio', 'tags', self.gf('tagging.fields.TagField')(null=True))

        # Changing field 'Audio.content'
        db.alter_column('mediasources_audio', 'content', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Audio.caption'
        db.alter_column('mediasources_audio', 'caption', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'VimeoVideo._api_data'
        db.alter_column('mediasources_vimeovideo', '_api_data', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'VimeoVideo.tags'
        db.alter_column('mediasources_vimeovideo', 'tags', self.gf('tagging.fields.TagField')(null=True))

        # Changing field 'VimeoVideo.content'
        db.alter_column('mediasources_vimeovideo', 'content', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'VimeoVideo.caption'
        db.alter_column('mediasources_vimeovideo', 'caption', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'VimeoVideo._oembed_data'
        db.alter_column('mediasources_vimeovideo', '_oembed_data', self.gf('django.db.models.fields.TextField')(null=True))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'media.attachedmediaitem': {
            'Meta': {'ordering': "[u'order']", 'object_name': 'AttachedMediaItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'attachedmediaitem_parent_set'", 'to': "orm['contenttypes.ContentType']"}),
            'parent_object_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'mediasources.audio': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'Audio'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'audio_created_by_user'", 'to': "orm['auth.User']"}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'audio_publish_by_user'", 'null': 'True', 'to': "orm['auth.User']"}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'audio_updated_by_user'", 'to': "orm['auth.User']"})
        },
        'mediasources.document': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'Document'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'document_created_by_user'", 'to': "orm['auth.User']"}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_processed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'document_publish_by_user'", 'null': 'True', 'to': "orm['auth.User']"}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'document_updated_by_user'", 'to': "orm['auth.User']"})
        },
        'mediasources.image': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'Image'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'image_created_by_user'", 'to': "orm['auth.User']"}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_processed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'image_publish_by_user'", 'null': 'True', 'to': "orm['auth.User']"}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'image_updated_by_user'", 'to': "orm['auth.User']"})
        },
        'mediasources.video': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'Video'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'video_created_by_user'", 'to': "orm['auth.User']"}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_processed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'video_publish_by_user'", 'null': 'True', 'to': "orm['auth.User']"}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'video_updated_by_user'", 'to': "orm['auth.User']"})
        },
        'mediasources.vimeovideo': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'VimeoVideo'},
            '_api_data': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            '_oembed_data': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'vimeovideo_created_by_user'", 'to': "orm['auth.User']"}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_processed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'vimeovideo_publish_by_user'", 'null': 'True', 'to': "orm['auth.User']"}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'vimeovideo_updated_by_user'", 'to': "orm['auth.User']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'mediasources.youtubevideo': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'YoutubeVideo'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'youtubevideo_created_by_user'", 'to': "orm['auth.User']"}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_processed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'youtubevideo_publish_by_user'", 'null': 'True', 'to': "orm['auth.User']"}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'youtubevideo_updated_by_user'", 'to': "orm['auth.User']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mediasources']