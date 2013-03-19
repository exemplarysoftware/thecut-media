# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from sorl.thumbnail import get_thumbnail
from thecut.authorship.admin import AuthorshipMixin
from thecut.media import settings
from thecut.media.mediasources.forms import (
    AudioAdminForm, DocumentAdminForm, ImageAdminForm, VideoAdminForm,
    YoutubeVideoAdminForm, VimeoVideoAdminForm)
from thecut.media.mediasources.models import (Audio, Document, Image, Video,
                                              YoutubeVideo, VimeoVideo)
from thecut.media.mediasources.views import UploadView


def conditionally_register(model, adminclass):
    """Register model with admin site if it is in MEDIA_SOURCES."""
    if 'thecut.media.mediasources.models.{0}'.format(model.__name__) in \
        settings.MEDIA_SOURCES:
        admin.site.register(model, adminclass)


def preview_image(obj):
    html = ''
    if hasattr(obj, 'get_image'):
        try:
            thumb = get_thumbnail(obj.get_image(), '100x75')
        except:
            pass
        else:
            html = '<span class="image-preview"><img src="{0}" alt="{1}" />' \
                   '</span>'.format(thumb.url, obj)
    return html
preview_image.short_description = 'Preview'
preview_image.allow_tags = True


class MediaUploadMixin(object):

    def add_view(self, request, form_url='', extra_context=None):
        view = UploadView.as_view()
        response = view(request, admin=self)
        return hasattr(response, 'render') and callable(response.render) and \
            response.render() or response


class AudioAdmin(MediaUploadMixin, AuthorshipMixin, admin.ModelAdmin):

    fieldsets = (
        (None, {'fields': ('file', 'title', 'caption', 'content', 'tags')}),
        ('Publishing', {'fields': (('publish_at', 'is_enabled'), 'expire_at',
                                   'publish_by', 'is_featured',
                                   ('created_at', 'created_by'),
                                   ('updated_at', 'updated_by')),
                        'classes': ('collapse',)}),
    )
    form = AudioAdminForm
    list_display = ('title', 'publish_at', 'is_enabled', 'is_featured',
                    preview_image)
    list_filter = ('publish_at', 'is_enabled', 'is_featured')
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    search_fields = ('title',)

conditionally_register(Audio, AudioAdmin)


class DocumentAdmin(MediaUploadMixin, AuthorshipMixin, admin.ModelAdmin):

    fieldsets = (
        (None, {'fields': ('file', 'title', 'caption', 'content', 'tags')}),
        ('Publishing', {'fields': (('publish_at', 'is_enabled'), 'expire_at',
                                   'publish_by', 'is_featured',
                                   ('created_at', 'created_by'),
                                   ('updated_at', 'updated_by')),
                        'classes': ('collapse',)}),
    )
    form = DocumentAdminForm
    list_display = ('title', 'publish_at', 'is_enabled', 'is_featured',
                    preview_image)
    list_filter = ('publish_at', 'is_enabled', 'is_featured')
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    search_fields = ('title',)

conditionally_register(Document, DocumentAdmin)


class ImageAdmin(MediaUploadMixin, AuthorshipMixin, admin.ModelAdmin):

    fieldsets = (
        (None, {'fields': ('file', 'title', 'caption', 'content', 'tags')}),
        ('Publishing', {'fields': (('publish_at', 'is_enabled'), 'expire_at',
                                   'publish_by', 'is_featured',
                                   ('created_at', 'created_by'),
                                   ('updated_at', 'updated_by')),
                        'classes': ('collapse',)}),
    )
    form = ImageAdminForm
    list_display = ('title', 'publish_at', 'is_enabled', 'is_featured',
                    preview_image)
    list_filter = ('publish_at', 'is_enabled', 'is_featured')
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    search_fields = ('title',)

conditionally_register(Image, ImageAdmin)


class VideoAdmin(MediaUploadMixin, AuthorshipMixin, admin.ModelAdmin):

    fieldsets = (
        (None, {'fields': ('file', 'title', 'caption', 'content', 'tags')}),
        ('Publishing', {'fields': (('publish_at', 'is_enabled'), 'expire_at',
                                   'publish_by', 'is_featured',
                                   ('created_at', 'created_by'),
                                   ('updated_at', 'updated_by')),
                        'classes': ('collapse',)}),
    )
    form = VideoAdminForm
    list_display = ('title', 'publish_at', 'is_enabled', 'is_featured',
                    preview_image)
    list_filter = ('publish_at', 'is_enabled', 'is_featured')
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    search_fields = ('title',)

conditionally_register(Video, VideoAdmin)


class YoutubeVideoAdmin(AuthorshipMixin, admin.ModelAdmin):

    fieldsets = (
        (None, {'fields': ('url', 'title', 'caption', 'content', 'tags')}),
        ('Publishing', {'fields': (('publish_at', 'is_enabled'), 'expire_at',
                                   'publish_by', 'is_featured',
                                   ('created_at', 'created_by'),
                                   ('updated_at', 'updated_by')),
                        'classes': ('collapse',)}),
    )
    form = YoutubeVideoAdminForm
    list_display = ('title', 'publish_at', 'is_enabled', 'is_featured',
                    preview_image)
    list_filter = ('publish_at', 'is_enabled', 'is_featured')
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    search_fields = ('title',)

conditionally_register(YoutubeVideo, YoutubeVideoAdmin)


class VimeoVideoAdmin(AuthorshipMixin, admin.ModelAdmin):

    fieldsets = (
        (None, {'fields': ('url', 'title', 'caption', 'content', 'tags')}),
        ('Publishing', {'fields': (('publish_at', 'is_enabled'), 'expire_at',
                                   'publish_by', 'is_featured',
                                   ('created_at', 'created_by'),
                                   ('updated_at', 'updated_by')),
                        'classes': ('collapse',)}),
    )
    form = VimeoVideoAdminForm
    list_display = ('title', 'publish_at', 'is_enabled', 'is_featured',
        preview_image)
    list_filter = ('publish_at', 'is_enabled', 'is_featured')
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    search_fields = ('title',)

conditionally_register(VimeoVideo, VimeoVideoAdmin)
