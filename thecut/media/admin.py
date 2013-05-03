# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from django.contrib.contenttypes.generic import GenericStackedInline
from thecut.media import views
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
                views.AdminContentTypeList.as_view()),
            url(r'^(?:\d+|add)/media/contenttype/(?P<content_type_pk>\d+)/picker$',
                views.AdminContentTypeObjectList.as_view()),
            url(r'^(?:\d+|add)/media/contenttype/(?P<content_type_pk>\d+)/list$',
                views.AdminContentTypeSelectedObjectList.as_view()),
        )
        urlpatterns += super(AttachedMediaItemMixin, self).get_urls()
        return urlpatterns
