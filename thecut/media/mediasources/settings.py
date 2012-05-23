# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf import settings
from sorl.thumbnail.conf import settings as sorl_settings


CELERY = 'djcelery' in settings.INSTALLED_APPS

GENERATE_THUMBNAILS_ON_SAVE = CELERY and getattr(settings,
    'MEDIASOURCES_GENERATE_THUMBNAILS_ON_SAVE', not settings.DEBUG)

STATIC_ROOT = getattr(settings, 'STATIC_ROOT', settings.MEDIA_ROOT)

STATICFILES_STORAGE = getattr(settings, 'STATICFILES_STORAGE', False)

PLACEHOLDER_IMAGE_PATH = getattr(settings,
    'MEDIASOURCES_PLACEHOLDER_IMAGE_PATH', 'media/placeholder.%s' %(
        'svg' if not 'pil_engine' in sorl_settings.THUMBNAIL_ENGINE else 'png'))

ADMIN_IMAGE_THUMBNAILS = getattr(settings,
    'MEDIASOURCES_ADMIN_IMAGE_THUMBNAILS', [
    # List of tuples containing geometry_size and options dict
    ('60x45', {'crop': 'center'}),
    ('100x75', {}),
    ('140x106', {'crop': 'center'}),
])

IMAGE_THUMBNAILS = ADMIN_IMAGE_THUMBNAILS + getattr(settings,
    'MEDIASOURCES_IMAGE_THUMBNAILS', [])


ADMIN_DOCUMENT_THUMBNAILS = getattr(settings,
    'MEDIASOURCES_ADMIN_DOCUMENT_THUMBNAILS', [
    # List of tuples containing geometry_size and options dict
    ('100x75', {}),
])

DOCUMENT_THUMBNAILS = ADMIN_DOCUMENT_THUMBNAILS + getattr(settings,
    'MEDIASOURCES_DOCUMENT_THUMBNAILS', [])


ADMIN_VIDEO_THUMBNAILS = getattr(settings,
    'MEDIASOURCES_ADMIN_VIDEO_THUMBNAILS', [
    # List of tuples containing geometry_size and options dict
    ('60x45', {'crop': 'center'}),
    ('100x75', {}),
    ('140x106', {'crop': 'center'}),
])

VIDEO_THUMBNAILS = ADMIN_VIDEO_THUMBNAILS + getattr(settings,
    'MEDIASOURCES_VIDEO_THUMBNAILS', [])

YOUTUBE_VIDEO_THUMBNAILS = ADMIN_VIDEO_THUMBNAILS + getattr(settings,
    'MEDIASOURCES_YOUTUBE_VIDEO_THUMBNAILS', [])

VIMEO_VIDEO_THUMBNAILS = ADMIN_VIDEO_THUMBNAILS + getattr(settings,
    'MEDIASOURCES_VIMEO_VIDEO_THUMBNAILS', [])


try:
    from exiftool import ExifTool
except ImportError:
    EXIFTOOL = False
else:
    EXIFTOOL = True

USE_EXIFTOOL = EXIFTOOL and getattr(settings, 'MEDIASOURCES_USE_EXIFTOOL', True)

