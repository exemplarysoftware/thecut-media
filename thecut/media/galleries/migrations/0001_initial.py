# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from thecut.authorship.settings import AUTH_USER_MODEL

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'Gallery'
        db.create_table('galleries_gallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('publish_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('expire_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('publish_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='gallery_publish_by_user', null=True, to=orm[AUTH_USER_MODEL])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='gallery_created_by_user', to=orm[AUTH_USER_MODEL])),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='gallery_updated_by_user', to=orm[AUTH_USER_MODEL])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('featured_content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('is_indexable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('tags', self.gf('tagging.fields.TagField')(null=True)),
            ('template', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('galleries', ['Gallery'])

        # Adding M2M table for field sites on 'Gallery'
        db.create_table('galleries_gallery_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gallery', models.ForeignKey(orm['galleries.gallery'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('galleries_gallery_sites', ['gallery_id', 'site_id'])


    def backwards(self, orm):

        # Deleting model 'Gallery'
        db.delete_table('galleries_gallery')

        # Removing M2M table for field sites on 'Gallery'
        db.delete_table('galleries_gallery_sites')


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
        'galleries.gallery': {
            'Meta': {'ordering': "['-publish_at', 'title']", 'object_name': 'Gallery'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gallery_created_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'featured_content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_indexable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'gallery_publish_by_user'", 'null': 'True', 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {'null': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gallery_updated_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['galleries']
