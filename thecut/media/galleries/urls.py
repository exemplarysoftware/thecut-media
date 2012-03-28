# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls.defaults import include, patterns, url
from thecut.media.galleries.feeds import LatestGalleryFeed
from thecut.media.galleries.views import ListView, MediaListView


urls = patterns('thecut.media.galleries.views',
    url(r'^$',
        ListView.as_view(), name='gallery_list'),
    url(r'^(?P<page>\d+)$',
        ListView.as_view(), name='paginated_gallery_list'),
    url(r'^latest\.xml$',
        LatestGalleryFeed(), name='gallery_feed'),
    
    url(r'^(?P<slug>[\w-]+)/$',
        MediaListView.as_view(), name='gallery_media_list'),
    url(r'^(?P<slug>[\w-]+)/(?P<page>\d+)$',
        MediaListView.as_view(), name='paginated_gallery_media_list'),
)

urlpatterns = patterns('',
    (r'^', include(urls, namespace='galleries')),
)

