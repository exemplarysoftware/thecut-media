# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from thecut.authorship.settings import AUTH_USER_MODEL

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        models = ['mediasources.Document', 'mediasources.Image',
            'mediasources.Video', 'mediasources.YoutubeVideo',
            'mediasources.VimeoVideo', 'mediasources.Audio']
        fields = ['tags', 'content', 'caption']
        extra_vimeo_fields = ['_api_data', '_oembed_data']

        for model in models:
            for obj in orm[model].objects.all():
                altered = False
                for field in fields:
                    if getattr(obj, field) is None:
                        setattr(obj, field, u'')
                        altered = True
                if altered:
                    obj.save()

        for obj in orm['mediasources.VimeoVideo'].objects.all():
            altered = False
            for field in extra_vimeo_fields:
                if getattr(obj, field) is None:
                    setattr(obj, field, u'')
                    altered = True
                if altered:
                    obj.save()


    def backwards(self, orm):
        pass


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
        AUTH_USER_MODEL: {
            'Meta': {'object_name': AUTH_USER_MODEL.split('.')[-1]},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'audio_created_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'audio_publish_by_user'", 'null': 'True', 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'audio_updated_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)})
        },
        'mediasources.document': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'Document'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'document_created_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_processed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'document_publish_by_user'", 'null': 'True', 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'document_updated_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)})
        },
        'mediasources.image': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'Image'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'image_created_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_processed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'image_publish_by_user'", 'null': 'True', 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'image_updated_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)})
        },
        'mediasources.video': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'Video'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'video_created_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_processed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'video_publish_by_user'", 'null': 'True', 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'video_updated_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)})
        },
        'mediasources.vimeovideo': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'VimeoVideo'},
            '_api_data': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            '_oembed_data': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'vimeovideo_created_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_processed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'vimeovideo_publish_by_user'", 'null': 'True', 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'vimeovideo_updated_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'mediasources.youtubevideo': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'YoutubeVideo'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'youtubevideo_created_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_processed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'youtubevideo_publish_by_user'", 'null': 'True', 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'tags': ('tagging.fields.TagField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'youtubevideo_updated_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mediasources']
