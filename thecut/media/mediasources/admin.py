# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import settings
from ..utils import get_preview_thumbnail
from .forms import (AudioAdminForm, DocumentAdminForm, ImageAdminForm,
                    VideoAdminForm, YoutubeVideoAdminForm, VimeoVideoAdminForm)
from .models import Audio, Document, Image, Video, YoutubeVideo, VimeoVideo
from .views import UploadView
from django.contrib import admin
from django.utils.functional import LazyObject
from thecut.authorship.admin import AuthorshipMixin


def preview_image(obj):
    html = ''
    if hasattr(obj, 'get_image'):
        try:
            thumb = get_preview_thumbnail(obj.get_image())
        except:
            pass
        else:
            html = '<span class="image-preview"><img src="{0}" alt="{1}" />' \
                   '</span>'.format(thumb.url, obj)
    return html
preview_image.short_description = 'Preview'
preview_image.allow_tags = True


class AdminMediaMixin(object):

    class Media(object):
        css = {'all': ['media/mediasources/image-preview.css']}


class MediaUploadMixin(object):

    def add_view(self, request, form_url='', extra_context=None):
        field = self.model._meta.get_field('file')

        view = UploadView.as_view()
        if settings.USE_S3UPLOAD:
            from .views.dropzone import DropzoneUploadView
            from storages.backends.s3boto import S3BotoStorage
            storage = field.storage
            if isinstance(storage, LazyObject):
                # Unwrap lazy storage
                storage._setup()
                storage = storage._wrapped
            if isinstance(storage, S3BotoStorage):
                view = DropzoneUploadView.as_view()

        response = view(request, admin=self)
        return hasattr(response, 'render') and callable(response.render) and \
            response.render() or response


class AudioAdmin(MediaUploadMixin, AuthorshipMixin, AdminMediaMixin,
                 admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['file', 'title', 'caption', 'content', 'tags']}),
        ('Publishing', {'fields': [('publish_at', 'is_enabled'), 'expire_at',
                                   'publish_by', 'is_featured',
                                   ('created_at', 'created_by'),
                                   ('updated_at', 'updated_by')],
                        'classes': ['collapse']}),
    ]

    form = AudioAdminForm

    list_display = ['title', 'updated_at', 'is_enabled', 'is_featured']

    list_filter = ['updated_at', 'is_enabled', 'is_featured']

    readonly_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']

    search_fields = ['title']

admin.site.register(Audio, AudioAdmin)


class DocumentAdmin(MediaUploadMixin, AuthorshipMixin, AdminMediaMixin,
                    admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['file', 'title', 'caption', 'content', 'tags']}),
        ('Publishing', {'fields': [('publish_at', 'is_enabled'), 'expire_at',
                                   'publish_by', 'is_featured',
                                   ('created_at', 'created_by'),
                                   ('updated_at', 'updated_by')],
                        'classes': ['collapse']}),
    ]

    form = DocumentAdminForm

    list_display = ['title', 'updated_at', 'is_enabled', 'is_featured']

    list_filter = ['updated_at', 'is_enabled', 'is_featured']

    readonly_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']

    search_fields = ['title']

admin.site.register(Document, DocumentAdmin)


class ImageAdmin(MediaUploadMixin, AuthorshipMixin, AdminMediaMixin,
                 admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['file', 'title', 'caption', 'content', 'tags']}),
        ('Publishing', {'fields': [('publish_at', 'is_enabled'), 'expire_at',
                                   'publish_by', 'is_featured',
                                   ('created_at', 'created_by'),
                                   ('updated_at', 'updated_by')],
                        'classes': ['collapse']}),
    ]

    form = ImageAdminForm

    list_display = ['title', 'updated_at', 'is_enabled', 'is_featured',
                    preview_image]

    list_filter = ['updated_at', 'is_enabled', 'is_featured']

    readonly_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']

    search_fields = ['title']

admin.site.register(Image, ImageAdmin)


class VideoAdmin(MediaUploadMixin, AuthorshipMixin, AdminMediaMixin,
                 admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['file', 'title', 'caption', 'content', 'tags']}),
        ('Publishing', {'fields': [('publish_at', 'is_enabled'), 'expire_at',
                                   'publish_by', 'is_featured',
                                   ('created_at', 'created_by'),
                                   ('updated_at', 'updated_by')],
                        'classes': ['collapse']}),
    ]

    form = VideoAdminForm

    list_display = ['title', 'updated_at', 'is_enabled', 'is_featured',
                    preview_image]

    list_filter = ['updated_at', 'is_enabled', 'is_featured']

    readonly_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']

    search_fields = ['title']

admin.site.register(Video, VideoAdmin)


class YoutubeVideoAdmin(AuthorshipMixin, AdminMediaMixin, admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['url', 'title', 'caption', 'content', 'tags']}),
        ('Publishing', {'fields': [('publish_at', 'is_enabled'), 'expire_at',
                                   'publish_by', 'is_featured',
                                   ('created_at', 'created_by'),
                                   ('updated_at', 'updated_by')],
                        'classes': ['collapse']}),
    ]

    form = YoutubeVideoAdminForm

    list_display = ['title', 'updated_at', 'is_enabled', 'is_featured',
                    preview_image]

    list_filter = ['updated_at', 'is_enabled', 'is_featured']

    readonly_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']

    search_fields = ['title']

admin.site.register(YoutubeVideo, YoutubeVideoAdmin)


class VimeoVideoAdmin(AuthorshipMixin, AdminMediaMixin, admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['url', 'title', 'caption', 'content', 'tags']}),
        ('Publishing', {'fields': [('publish_at', 'is_enabled'), 'expire_at',
                                   'publish_by', 'is_featured',
                                   ('created_at', 'created_by'),
                                   ('updated_at', 'updated_by')],
                        'classes': ['collapse']}),
    ]

    form = VimeoVideoAdminForm

    list_display = ['title', 'updated_at', 'is_enabled', 'is_featured',
                    preview_image]

    list_filter = ['updated_at', 'is_enabled', 'is_featured']

    readonly_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']

    search_fields = ['title']

admin.site.register(VimeoVideo, VimeoVideoAdmin)
