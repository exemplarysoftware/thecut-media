# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import include, url
from thecut.media.galleries import feeds, views


urls = [

    url(r'^$',
        views.ListView.as_view(), name='gallery_list'),
    url(r'^(?P<page>\d+)$',
        views.ListView.as_view(), name='paginated_gallery_list'),
    url(r'^latest\.xml$',
        feeds.LatestGalleryFeed(), name='gallery_feed'),

    url(r'^categories/(?P<slug>[\w-]+)/$',
        views.ListView.as_view(), name='category_gallery_list'),
    url(r'^categories/(?P<slug>[\w-]+)/(?P<page>\d+)$',
        views.ListView.as_view(), name='paginated_category_gallery_list'),
    url(r'^categories/(?P<slug>[\w-]+)/latest\.xml$',
        feeds.LatestCategoryGalleryFeed(), name='category_gallery_feed'),

    url(r'^(?P<slug>[\w-]+)/$',
        views.MediaListView.as_view(), name='gallery_media_list'),
    url(r'^(?P<slug>[\w-]+)/(?P<page>\d+)$',
        views.MediaListView.as_view(), name='paginated_gallery_media_list'),

]

urlpatterns = [url(r'^', include(urls, namespace='galleries'))]
