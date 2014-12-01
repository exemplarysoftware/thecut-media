# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import thecut.media.mediasources.models
import django.utils.timezone
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_enabled', models.BooleanField(default=True, db_index=True, verbose_name='enabled')),
                ('is_featured', models.BooleanField(default=False, db_index=True, verbose_name='featured')),
                ('publish_at', models.DateTimeField(default=django.utils.timezone.now, help_text='This item will only be viewable on the website if it is enabled, and this date and time has past.', verbose_name='publish date & time', db_index=True)),
                ('expire_at', models.DateTimeField(help_text='This item will no longer be viewable on the website if this date and time has past. Leave blank if you do not wish this item to expire.', null=True, verbose_name='expiry date & time', db_index=True, blank=True)),
                ('title', models.CharField(max_length=200, db_index=True)),
                ('caption', models.TextField(default='', blank=True)),
                ('content', models.TextField(default='', blank=True)),
                ('file', models.FileField(max_length=250, upload_to='uploads/media/audios/%Y/%m/%d')),
                ('created_by', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
                ('publish_by', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('updated_by', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
                'get_latest_by': 'publish_at',
            },
            bases=(thecut.media.mediasources.models.IsProcessedMixin, thecut.media.mediasources.models.FileMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_enabled', models.BooleanField(default=True, db_index=True, verbose_name='enabled')),
                ('is_featured', models.BooleanField(default=False, db_index=True, verbose_name='featured')),
                ('publish_at', models.DateTimeField(default=django.utils.timezone.now, help_text='This item will only be viewable on the website if it is enabled, and this date and time has past.', verbose_name='publish date & time', db_index=True)),
                ('expire_at', models.DateTimeField(help_text='This item will no longer be viewable on the website if this date and time has past. Leave blank if you do not wish this item to expire.', null=True, verbose_name='expiry date & time', db_index=True, blank=True)),
                ('title', models.CharField(max_length=200, db_index=True)),
                ('caption', models.TextField(default='', blank=True)),
                ('content', models.TextField(default='', blank=True)),
                ('file', models.FileField(max_length=250, upload_to='uploads/media/documents/%Y/%m/%d')),
                ('created_by', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
                ('publish_by', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('updated_by', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
                'get_latest_by': 'publish_at',
            },
            bases=(thecut.media.mediasources.models.IsProcessedMixin, thecut.media.mediasources.models.FileMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_enabled', models.BooleanField(default=True, db_index=True, verbose_name='enabled')),
                ('is_featured', models.BooleanField(default=False, db_index=True, verbose_name='featured')),
                ('publish_at', models.DateTimeField(default=django.utils.timezone.now, help_text='This item will only be viewable on the website if it is enabled, and this date and time has past.', verbose_name='publish date & time', db_index=True)),
                ('expire_at', models.DateTimeField(help_text='This item will no longer be viewable on the website if this date and time has past. Leave blank if you do not wish this item to expire.', null=True, verbose_name='expiry date & time', db_index=True, blank=True)),
                ('title', models.CharField(max_length=200, db_index=True)),
                ('caption', models.TextField(default='', blank=True)),
                ('content', models.TextField(default='', blank=True)),
                ('file', models.ImageField(max_length=250, upload_to='uploads/media/images/%Y/%m/%d')),
                ('created_by', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
                ('publish_by', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('updated_by', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
                'get_latest_by': 'publish_at',
            },
            bases=(thecut.media.mediasources.models.IsProcessedMixin, thecut.media.mediasources.models.FileMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_enabled', models.BooleanField(default=True, db_index=True, verbose_name='enabled')),
                ('is_featured', models.BooleanField(default=False, db_index=True, verbose_name='featured')),
                ('publish_at', models.DateTimeField(default=django.utils.timezone.now, help_text='This item will only be viewable on the website if it is enabled, and this date and time has past.', verbose_name='publish date & time', db_index=True)),
                ('expire_at', models.DateTimeField(help_text='This item will no longer be viewable on the website if this date and time has past. Leave blank if you do not wish this item to expire.', null=True, verbose_name='expiry date & time', db_index=True, blank=True)),
                ('title', models.CharField(max_length=200, db_index=True)),
                ('caption', models.TextField(default='', blank=True)),
                ('content', models.TextField(default='', blank=True)),
                ('file', models.FileField(max_length=250, upload_to='uploads/media/videos/%Y/%m/%d')),
                ('created_by', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
                ('publish_by', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('updated_by', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
                'get_latest_by': 'publish_at',
            },
            bases=(thecut.media.mediasources.models.IsProcessedMixin, thecut.media.mediasources.models.FileMixin, models.Model),
        ),
        migrations.CreateModel(
            name='VimeoVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_enabled', models.BooleanField(default=True, db_index=True, verbose_name='enabled')),
                ('is_featured', models.BooleanField(default=False, db_index=True, verbose_name='featured')),
                ('publish_at', models.DateTimeField(default=django.utils.timezone.now, help_text='This item will only be viewable on the website if it is enabled, and this date and time has past.', verbose_name='publish date & time', db_index=True)),
                ('expire_at', models.DateTimeField(help_text='This item will no longer be viewable on the website if this date and time has past. Leave blank if you do not wish this item to expire.', null=True, verbose_name='expiry date & time', db_index=True, blank=True)),
                ('title', models.CharField(max_length=200, db_index=True)),
                ('caption', models.TextField(default='', blank=True)),
                ('content', models.TextField(default='', blank=True)),
                ('url', models.URLField(help_text='e.g. http://vimeo.com/123456')),
                ('_api_data', models.TextField(default='', editable=False, blank=True)),
                ('_oembed_data', models.TextField(default='', editable=False, blank=True)),
                ('created_by', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
                ('publish_by', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('updated_by', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
                'get_latest_by': 'publish_at',
            },
            bases=(thecut.media.mediasources.models.IsProcessedMixin, models.Model),
        ),
        migrations.CreateModel(
            name='YoutubeVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_enabled', models.BooleanField(default=True, db_index=True, verbose_name='enabled')),
                ('is_featured', models.BooleanField(default=False, db_index=True, verbose_name='featured')),
                ('publish_at', models.DateTimeField(default=django.utils.timezone.now, help_text='This item will only be viewable on the website if it is enabled, and this date and time has past.', verbose_name='publish date & time', db_index=True)),
                ('expire_at', models.DateTimeField(help_text='This item will no longer be viewable on the website if this date and time has past. Leave blank if you do not wish this item to expire.', null=True, verbose_name='expiry date & time', db_index=True, blank=True)),
                ('title', models.CharField(max_length=200, db_index=True)),
                ('caption', models.TextField(default='', blank=True)),
                ('content', models.TextField(default='', blank=True)),
                ('url', models.URLField()),
                ('created_by', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
                ('publish_by', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('updated_by', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
                'get_latest_by': 'publish_at',
            },
            bases=(thecut.media.mediasources.models.IsProcessedMixin, models.Model),
        ),
    ]
