# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import views
from django.conf.urls import include, patterns, url
from rest_framework.urlpatterns import format_suffix_patterns


def generate_urls(media_models):

    urls = patterns(
        'thecut.media.api.views',

        url(r'^$', views.MediaRootAPIView.as_view(),
            {'media_models': media_models}, name='root'),

        url(r'^contenttypes/$',
            views.ContentTypeListAPIView.as_view(),
            {'media_models': media_models}, name='contenttype_list'),

        url(r'^contenttypes/(?P<pk>\d+)/$',
            views.ContentTypeRetrieveAPIView.as_view(),
            {'media_models': media_models}, name='contenttype_detail'),

        url(r'^contenttypes/(?P<contenttype_pk>\d+)/objects/$',
            views.ContentTypeObjectListAPIView.as_view(),
            {'media_models': media_models}, name='contenttype_object_list'),

        url(r'^contenttypes/(?P<contenttype_pk>\d+)/objects/(?P<pk>\d+)/$',
            views.ContentTypeObjectDetailAPIView.as_view(),
            {'media_models': media_models},
            name='contenttype_object_detail'),

    )

    urlpatterns = patterns(
        '', (r'^', include(urls, namespace='media_api')))

    urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

    return urlpatterns
