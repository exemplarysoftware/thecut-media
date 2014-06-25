# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import views
from .forms import AttachedMediaItemInlineForm
from .models import AttachedMediaItem
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.contrib.contenttypes.generic import GenericStackedInline


class AttachedMediaItemInline(GenericStackedInline):

    ct_field = 'parent_content_type'

    ct_fk_field = 'parent_object_id'

    extra = 0

    form = AttachedMediaItemInlineForm

    model = AttachedMediaItem


class AttachedMediaItemMixin(admin.ModelAdmin):

    inlines = [AttachedMediaItemInline]

    def get_urls(self):
        urlpatterns = patterns(
            'thecut.media.views',
            url(r'^(?:\d+|add)/media/contenttype/$',
                views.AdminContentTypeList.as_view()),
            url(r'^(?:\d+|add)/media/contenttype/(?P<content_type_pk>\d+)'
                '/picker$',
                views.AdminContentTypeObjectList.as_view()),
            url(r'^(?:\d+|add)/media/contenttype/(?P<content_type_pk>\d+)'
                '/list$',
                views.AdminContentTypeSelectedObjectList.as_view()),
            (r'^media/api/', include('thecut.media.api.urls')),
        )
        urlpatterns += super(AttachedMediaItemMixin, self).get_urls()
        return urlpatterns
