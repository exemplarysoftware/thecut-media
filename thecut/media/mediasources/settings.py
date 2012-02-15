# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf import settings


CELERY = 'djcelery' in settings.INSTALLED_APPS


ADMIN_IMAGE_THUMBNAILS = getattr(settings,
    'MEDIASOURCES_ADMIN_IMAGE_THUMBNAILS', [
    # List of tuples containing geometry_size and options dict
    ('60x45', {'crop': 'center'}),
    ('100x75', {'crop': 'center'}),
    ('140x106', {'crop': 'center'}),
])

IMAGE_THUMBNAILS = ADMIN_IMAGE_THUMBNAILS + getattr(settings,
    'MEDIASOURCES_IMAGE_THUMBNAILS', [])


DOCUMENT_THUMBNAILS = getattr(settings,
    'MEDIASOURCES_DOCUMENT_THUMBNAILS', [])


ADMIN_VIDEO_THUMBNAILS = getattr(settings,
    'MEDIASOURCES_ADMIN_VIDEO_THUMBNAILS', [
    # List of tuples containing geometry_size and options dict
    ('60x45', {'crop': 'center'}),
    ('100x75', {'crop': 'center'}),
    ('140x106', {'crop': 'center'}),
])

VIDEO_THUMBNAILS = ADMIN_VIDEO_THUMBNAILS + getattr(settings,
    'MEDIASOURCES_VIDEO_THUMBNAILS', [])

YOUTUBE_VIDEO_THUMBNAILS = ADMIN_VIDEO_THUMBNAILS + getattr(settings,
    'MEDIASOURCES_YOUTUBE_VIDEO_THUMBNAILS', [])

VIMEO_VIDEO_THUMBNAILS = ADMIN_VIDEO_THUMBNAILS + getattr(settings,
    'MEDIASOURCES_VIMEO_VIDEO_THUMBNAILS', [])

