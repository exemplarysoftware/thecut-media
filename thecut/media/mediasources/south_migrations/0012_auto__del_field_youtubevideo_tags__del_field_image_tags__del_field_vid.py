# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from thecut.authorship.settings import AUTH_USER_MODEL


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'YoutubeVideo.tags'
        db.delete_column(u'mediasources_youtubevideo', 'tags')

        # Deleting field 'Image.tags'
        db.delete_column(u'mediasources_image', 'tags')

        # Deleting field 'Video.tags'
        db.delete_column(u'mediasources_video', 'tags')

        # Deleting field 'Document.tags'
        db.delete_column(u'mediasources_document', 'tags')

        # Deleting field 'Audio.tags'
        db.delete_column(u'mediasources_audio', 'tags')

        # Deleting field 'VimeoVideo.tags'
        db.delete_column(u'mediasources_vimeovideo', 'tags')


    def backwards(self, orm):
        # Adding field 'YoutubeVideo.tags'
        db.add_column(u'mediasources_youtubevideo', 'tags',
                      self.gf('tagging.fields.TagField')(default=u''),
                      keep_default=False)

        # Adding field 'Image.tags'
        db.add_column(u'mediasources_image', 'tags',
                      self.gf('tagging.fields.TagField')(default=u''),
                      keep_default=False)

        # Adding field 'Video.tags'
        db.add_column(u'mediasources_video', 'tags',
                      self.gf('tagging.fields.TagField')(default=u''),
                      keep_default=False)

        # Adding field 'Document.tags'
        db.add_column(u'mediasources_document', 'tags',
                      self.gf('tagging.fields.TagField')(default=u''),
                      keep_default=False)

        # Adding field 'Audio.tags'
        db.add_column(u'mediasources_audio', 'tags',
                      self.gf('tagging.fields.TagField')(default=u''),
                      keep_default=False)

        # Adding field 'VimeoVideo.tags'
        db.add_column(u'mediasources_vimeovideo', 'tags',
                      self.gf('tagging.fields.TagField')(default=u''),
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
        AUTH_USER_MODEL: {
            'Meta': {'object_name': AUTH_USER_MODEL.split('.')[-1]},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mediasources.audio': {
            'Meta': {'ordering': "(u'-created_at',)", 'object_name': 'Audio'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['{0}']".format(AUTH_USER_MODEL)}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'+'", 'null': 'True', 'to': u"orm['{0}']".format(AUTH_USER_MODEL)}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['{0}']".format(AUTH_USER_MODEL)})
        },
        u'mediasources.document': {
            'Meta': {'ordering': "(u'-created_at',)", 'object_name': 'Document'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['{0}']".format(AUTH_USER_MODEL)}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'+'", 'null': 'True', 'to': u"orm['{0}']".format(AUTH_USER_MODEL)}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['{0}']".format(AUTH_USER_MODEL)})
        },
        u'mediasources.image': {
            'Meta': {'ordering': "(u'-created_at',)", 'object_name': 'Image'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['{0}']".format(AUTH_USER_MODEL)}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'+'", 'null': 'True', 'to': u"orm['{0}']".format(AUTH_USER_MODEL)}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['{0}']".format(AUTH_USER_MODEL)})
        },
        u'mediasources.video': {
            'Meta': {'ordering': "(u'-created_at',)", 'object_name': 'Video'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['{0}']".format(AUTH_USER_MODEL)}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'+'", 'null': 'True', 'to': u"orm['{0}']".format(AUTH_USER_MODEL)}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['{0}']".format(AUTH_USER_MODEL)})
        },
        u'mediasources.vimeovideo': {
            'Meta': {'ordering': "(u'-created_at',)", 'object_name': 'VimeoVideo'},
            '_api_data': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            '_oembed_data': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['{0}']".format(AUTH_USER_MODEL)}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'+'", 'null': 'True', 'to': u"orm['{0}']".format(AUTH_USER_MODEL)}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['{0}']".format(AUTH_USER_MODEL)}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'mediasources.youtubevideo': {
            'Meta': {'ordering': "(u'-created_at',)", 'object_name': 'YoutubeVideo'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['{0}']".format(AUTH_USER_MODEL)}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'+'", 'null': 'True', 'to': u"orm['{0}']".format(AUTH_USER_MODEL)}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['{0}']".format(AUTH_USER_MODEL)}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mediasources']
