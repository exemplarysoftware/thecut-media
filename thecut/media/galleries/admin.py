# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from sorl.thumbnail import get_thumbnail
from thecut.core.admin import ModelAdmin
from thecut.media.admin import AttachedMediaItemMixin
from thecut.media.galleries.forms import (GalleryAdminForm,
    GalleryCategoryAdminForm)
from thecut.media.galleries.models import Gallery, GalleryCategory


def preview_image(obj):
    image = obj.media.get_image()
    if image:
        thumb = get_thumbnail(image, '100x75')
        return '<img src="%s" alt="%s" />' %(thumb.url, unicode(obj))
    else:
        return ''
preview_image.short_description = 'Preview'
preview_image.allow_tags = True


class GalleryAdmin(AttachedMediaItemMixin, ModelAdmin):
    date_hierarchy = 'publish_at'
    fieldsets = [
        (None, {'fields': ['title', 'headline', 'featured_content', 'content',
            'meta_description', 'tags']}),
        ('Publishing', {'fields': ['categories', 'sites', 'slug',
            ('publish_at', 'is_enabled'), 'expire_at', 'publish_by',
            'template', 'is_featured', 'is_indexable',
            ('created_at', 'created_by'), ('updated_at', 'updated_by')],
            'classes': ['collapse']}),
    ]
    form = GalleryAdminForm
    list_display = ['title', 'publish_at', 'is_enabled', 'is_featured',
        'is_indexable', preview_image]
    list_filter = ['publish_at', 'is_enabled', 'is_featured', 'is_indexable']
    prepopulated_fields = {'slug': ['title']}
    readonly_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']
    search_fields = ['title']

admin.site.register(Gallery, GalleryAdmin)


class GalleryCategoryAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'headline', 'featured_content', 'content',
            'meta_description', 'tags']}),
        ('Publishing', {'fields': ['slug',
            ('publish_at', 'is_enabled'), 'expire_at', 'publish_by',
            'template', 'is_featured', 'is_indexable',
            ('created_at', 'created_by'), ('updated_at', 'updated_by')],
            'classes': ['collapse']}),
    ]
    form = GalleryCategoryAdminForm
    list_display = ['title', 'publish_at', 'is_enabled', 'is_featured',
        'is_indexable']
    list_filter = ['publish_at', 'is_enabled', 'is_featured', 'is_indexable']
    prepopulated_fields = {'slug': ['title']}
    readonly_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']
    search_fields = ['title']

admin.site.register(GalleryCategory, GalleryCategoryAdmin)

