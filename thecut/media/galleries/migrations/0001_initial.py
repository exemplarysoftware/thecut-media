# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import taggit.managers
import thecut.publishing.models


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_enabled', models.BooleanField(default=True, db_index=True, verbose_name='enabled')),
                ('is_featured', models.BooleanField(default=False, db_index=True, verbose_name='featured')),
                ('publish_at', models.DateTimeField(default=django.utils.timezone.now, help_text='This item will only be viewable on the website if it is enabled, and this date and time has past.', verbose_name='publish date & time', db_index=True)),
                ('expire_at', models.DateTimeField(help_text='This item will no longer be viewable on the website if this date and time has past. Leave blank if you do not wish this item to expire.', null=True, verbose_name='expiry date & time', db_index=True, blank=True)),
                ('title', models.CharField(max_length=200)),
                ('headline', models.CharField(default='', max_length=200, blank=True)),
                ('content', models.TextField(default='', blank=True)),
                ('featured_content', models.TextField(default='', blank=True)),
                ('is_indexable', models.BooleanField(default=True, help_text='Should this page be indexed by search engines?', db_index=True, verbose_name='indexable')),
                ('meta_description', models.CharField(default='', help_text='Optional short description for use by search engines.', max_length=200, blank=True)),
                ('template', models.CharField(default='', help_text='Example: "app/model_detail.html".', max_length=100, blank=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('-publish_at', 'title'),
                'abstract': False,
                'get_latest_by': 'publish_at',
                'verbose_name_plural': 'galleries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GalleryCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_enabled', models.BooleanField(default=True, db_index=True, verbose_name='enabled')),
                ('is_featured', models.BooleanField(default=False, db_index=True, verbose_name='featured')),
                ('publish_at', models.DateTimeField(default=django.utils.timezone.now, help_text='This item will only be viewable on the website if it is enabled, and this date and time has past.', verbose_name='publish date & time', db_index=True)),
                ('expire_at', models.DateTimeField(help_text='This item will no longer be viewable on the website if this date and time has past. Leave blank if you do not wish this item to expire.', null=True, verbose_name='expiry date & time', db_index=True, blank=True)),
                ('title', models.CharField(max_length=200)),
                ('headline', models.CharField(default='', max_length=200, blank=True)),
                ('content', models.TextField(default='', blank=True)),
                ('featured_content', models.TextField(default='', blank=True)),
                ('is_indexable', models.BooleanField(default=True, help_text='Should this page be indexed by search engines?', db_index=True, verbose_name='indexable')),
                ('meta_description', models.CharField(default='', help_text='Optional short description for use by search engines.', max_length=200, blank=True)),
                ('template', models.CharField(default='', help_text='Example: "app/model_detail.html".', max_length=100, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('created_by', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
                ('publish_by', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('updated_by', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('title',),
                'abstract': False,
                'get_latest_by': 'publish_at',
                'verbose_name_plural': 'gallery categories',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gallery',
            name='categories',
            field=models.ManyToManyField(related_name='galleries', null=True, to='galleries.GalleryCategory', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='created_by',
            field=models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='publish_by',
            field=models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='site',
            field=models.ForeignKey(default=thecut.publishing.models.get_current_site, to='sites.Site'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='updated_by',
            field=models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='gallery',
            unique_together=set([('site', 'slug')]),
        ),
    ]
