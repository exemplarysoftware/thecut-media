# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import views
from django.conf.urls import include, patterns, url
from rest_framework.urlpatterns import format_suffix_patterns


urls = patterns(
    'thecut.media.api.views',

    url(r'^$', views.MediaRootAPIView.as_view(), name='root'),

    url(r'^contenttypes/$',
        views.ContentTypeListAPIView.as_view(), name='contenttype_list'),

    url(r'^contenttypes/(?P<pk>\d+)/$',
        views.ContentTypeRetrieveAPIView.as_view(), name='contenttype_detail'),

    url(r'^contenttypes/(?P<pk>\d+)/objects/$',
        views.ContentTypeListAPIView.as_view(), name='contenttype_object_list'),

)


urlpatterns = patterns(
    '', (r'^', include(urls, namespace='media_api')))

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
