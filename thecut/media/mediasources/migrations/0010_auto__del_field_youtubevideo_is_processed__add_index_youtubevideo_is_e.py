# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'YoutubeVideo.is_processed'
        db.delete_column(u'mediasources_youtubevideo', 'is_processed')

        # Adding index on 'YoutubeVideo', fields ['is_enabled']
        db.create_index(u'mediasources_youtubevideo', ['is_enabled'])

        # Adding index on 'YoutubeVideo', fields ['is_featured']
        db.create_index(u'mediasources_youtubevideo', ['is_featured'])

        # Adding index on 'YoutubeVideo', fields ['publish_at']
        db.create_index(u'mediasources_youtubevideo', ['publish_at'])

        # Adding index on 'YoutubeVideo', fields ['expire_at']
        db.create_index(u'mediasources_youtubevideo', ['expire_at'])

        # Deleting field 'Image.is_processed'
        db.delete_column(u'mediasources_image', 'is_processed')

        # Adding index on 'Image', fields ['is_enabled']
        db.create_index(u'mediasources_image', ['is_enabled'])

        # Adding index on 'Image', fields ['is_featured']
        db.create_index(u'mediasources_image', ['is_featured'])

        # Adding index on 'Image', fields ['publish_at']
        db.create_index(u'mediasources_image', ['publish_at'])

        # Adding index on 'Image', fields ['expire_at']
        db.create_index(u'mediasources_image', ['expire_at'])

        # Deleting field 'Video.is_processed'
        db.delete_column(u'mediasources_video', 'is_processed')

        # Adding index on 'Video', fields ['is_enabled']
        db.create_index(u'mediasources_video', ['is_enabled'])

        # Adding index on 'Video', fields ['is_featured']
        db.create_index(u'mediasources_video', ['is_featured'])

        # Adding index on 'Video', fields ['publish_at']
        db.create_index(u'mediasources_video', ['publish_at'])

        # Adding index on 'Video', fields ['expire_at']
        db.create_index(u'mediasources_video', ['expire_at'])

        # Deleting field 'Document.is_processed'
        db.delete_column(u'mediasources_document', 'is_processed')

        # Adding index on 'Document', fields ['is_enabled']
        db.create_index(u'mediasources_document', ['is_enabled'])

        # Adding index on 'Document', fields ['is_featured']
        db.create_index(u'mediasources_document', ['is_featured'])

        # Adding index on 'Document', fields ['publish_at']
        db.create_index(u'mediasources_document', ['publish_at'])

        # Adding index on 'Document', fields ['expire_at']
        db.create_index(u'mediasources_document', ['expire_at'])

        # Adding index on 'Audio', fields ['is_enabled']
        db.create_index(u'mediasources_audio', ['is_enabled'])

        # Adding index on 'Audio', fields ['is_featured']
        db.create_index(u'mediasources_audio', ['is_featured'])

        # Adding index on 'Audio', fields ['publish_at']
        db.create_index(u'mediasources_audio', ['publish_at'])

        # Adding index on 'Audio', fields ['expire_at']
        db.create_index(u'mediasources_audio', ['expire_at'])

        # Deleting field 'VimeoVideo.is_processed'
        db.delete_column(u'mediasources_vimeovideo', 'is_processed')

        # Adding index on 'VimeoVideo', fields ['is_enabled']
        db.create_index(u'mediasources_vimeovideo', ['is_enabled'])

        # Adding index on 'VimeoVideo', fields ['is_featured']
        db.create_index(u'mediasources_vimeovideo', ['is_featured'])

        # Adding index on 'VimeoVideo', fields ['publish_at']
        db.create_index(u'mediasources_vimeovideo', ['publish_at'])

        # Adding index on 'VimeoVideo', fields ['expire_at']
        db.create_index(u'mediasources_vimeovideo', ['expire_at'])


    def backwards(self, orm):
        # Removing index on 'VimeoVideo', fields ['expire_at']
        db.delete_index(u'mediasources_vimeovideo', ['expire_at'])

        # Removing index on 'VimeoVideo', fields ['publish_at']
        db.delete_index(u'mediasources_vimeovideo', ['publish_at'])

        # Removing index on 'VimeoVideo', fields ['is_featured']
        db.delete_index(u'mediasources_vimeovideo', ['is_featured'])

        # Removing index on 'VimeoVideo', fields ['is_enabled']
        db.delete_index(u'mediasources_vimeovideo', ['is_enabled'])

        # Removing index on 'Audio', fields ['expire_at']
        db.delete_index(u'mediasources_audio', ['expire_at'])

        # Removing index on 'Audio', fields ['publish_at']
        db.delete_index(u'mediasources_audio', ['publish_at'])

        # Removing index on 'Audio', fields ['is_featured']
        db.delete_index(u'mediasources_audio', ['is_featured'])

        # Removing index on 'Audio', fields ['is_enabled']
        db.delete_index(u'mediasources_audio', ['is_enabled'])

        # Removing index on 'Document', fields ['expire_at']
        db.delete_index(u'mediasources_document', ['expire_at'])

        # Removing index on 'Document', fields ['publish_at']
        db.delete_index(u'mediasources_document', ['publish_at'])

        # Removing index on 'Document', fields ['is_featured']
        db.delete_index(u'mediasources_document', ['is_featured'])

        # Removing index on 'Document', fields ['is_enabled']
        db.delete_index(u'mediasources_document', ['is_enabled'])

        # Removing index on 'Video', fields ['expire_at']
        db.delete_index(u'mediasources_video', ['expire_at'])

        # Removing index on 'Video', fields ['publish_at']
        db.delete_index(u'mediasources_video', ['publish_at'])

        # Removing index on 'Video', fields ['is_featured']
        db.delete_index(u'mediasources_video', ['is_featured'])

        # Removing index on 'Video', fields ['is_enabled']
        db.delete_index(u'mediasources_video', ['is_enabled'])

        # Removing index on 'Image', fields ['expire_at']
        db.delete_index(u'mediasources_image', ['expire_at'])

        # Removing index on 'Image', fields ['publish_at']
        db.delete_index(u'mediasources_image', ['publish_at'])

        # Removing index on 'Image', fields ['is_featured']
        db.delete_index(u'mediasources_image', ['is_featured'])

        # Removing index on 'Image', fields ['is_enabled']
        db.delete_index(u'mediasources_image', ['is_enabled'])

        # Removing index on 'YoutubeVideo', fields ['expire_at']
        db.delete_index(u'mediasources_youtubevideo', ['expire_at'])

        # Removing index on 'YoutubeVideo', fields ['publish_at']
        db.delete_index(u'mediasources_youtubevideo', ['publish_at'])

        # Removing index on 'YoutubeVideo', fields ['is_featured']
        db.delete_index(u'mediasources_youtubevideo', ['is_featured'])

        # Removing index on 'YoutubeVideo', fields ['is_enabled']
        db.delete_index(u'mediasources_youtubevideo', ['is_enabled'])

        # Adding field 'YoutubeVideo.is_processed'
        db.add_column(u'mediasources_youtubevideo', 'is_processed',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Image.is_processed'
        db.add_column(u'mediasources_image', 'is_processed',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Video.is_processed'
        db.add_column(u'mediasources_video', 'is_processed',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Document.is_processed'
        db.add_column(u'mediasources_document', 'is_processed',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'VimeoVideo.is_processed'
        db.add_column(u'mediasources_vimeovideo', 'is_processed',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'media.attachedmediaitem': {
            'Meta': {'ordering': "(u'order',)", 'object_name': 'AttachedMediaItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'attachedmediaitem_parent_set'", 'to': u"orm['contenttypes.ContentType']"}),
            'parent_object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        u'mediasources.audio': {
            'Meta': {'ordering': "(u'-created_at',)", 'object_name': 'Audio'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['auth.User']"}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['auth.User']"})
        },
        u'mediasources.document': {
            'Meta': {'ordering': "(u'-created_at',)", 'object_name': 'Document'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['auth.User']"}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['auth.User']"})
        },
        u'mediasources.image': {
            'Meta': {'ordering': "(u'-created_at',)", 'object_name': 'Image'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['auth.User']"}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['auth.User']"})
        },
        u'mediasources.video': {
            'Meta': {'ordering': "(u'-created_at',)", 'object_name': 'Video'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['auth.User']"}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['auth.User']"})
        },
        u'mediasources.vimeovideo': {
            'Meta': {'ordering': "(u'-created_at',)", 'object_name': 'VimeoVideo'},
            '_api_data': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            '_oembed_data': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['auth.User']"}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['auth.User']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'mediasources.youtubevideo': {
            'Meta': {'ordering': "(u'-created_at',)", 'object_name': 'YoutubeVideo'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['auth.User']"}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['auth.User']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mediasources']