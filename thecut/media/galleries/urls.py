# -*- coding: utf-8 -*-
from django.conf.urls.defaults import include, patterns, url
from thecut.media.galleries.feeds import LatestGalleryFeed


urls = patterns('thecut.media.galleries.views',
    url(r'^$',
        'gallery_list', name='gallery_list'),
    url(r'^(?P<page>\d+)$',
        'gallery_list', name='paginated_gallery_list'),
    url(r'^latest\.xml$',
        LatestGalleryFeed(), name='gallery_feed'),
    
    url(r'^(?P<slug>[\w-]+)/$',
        'gallery_media_list', name='gallery_media_list'),
    url(r'^(?P<slug>[\w-]+)/(?P<page>\d+)$',
        'gallery_media_list', name='paginated_gallery_media_list'),
)

urlpatterns = patterns('',
    (r'^', include(urls, namespace='galleries')),
)

