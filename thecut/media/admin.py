# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from django.contrib.contenttypes.generic import GenericStackedInline
from thecut.media.forms import AttachedMediaItemInlineForm
from thecut.media.models import AttachedMediaItem

try:
    from django.conf.urls import patterns, url
except ImportError:
    # Pre-Django 1.4 compatibility
    from django.conf.urls.defaults import patterns, url


class AttachedMediaItemInline(GenericStackedInline):

    ct_field = 'parent_content_type'
    ct_fk_field = 'parent_object_id'
    extra = 0
    form = AttachedMediaItemInlineForm
    model = AttachedMediaItem


class AttachedMediaItemMixin(admin.ModelAdmin):

    inlines = (AttachedMediaItemInline,)

    def get_urls(self):
        urlpatterns = patterns('thecut.media.views',
            url(r'^(?:\d+|add)/media/contenttype/$',
                'admin_contenttype_list'),
            url(r'^(?:\d+|add)/media/contenttype/(?P<content_type_pk>\d+)/picker$',
                'admin_contenttype_object_list'),
            url(r'^(?:\d+|add)/media/contenttype/(?P<content_type_pk>\d+)/list$',
                'admin_contenttype_selected_object_list'),
        )
        urlpatterns += super(AttachedMediaItemMixin, self).get_urls()
        return urlpatterns
