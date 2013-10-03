# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf import settings
from thecut.media import settings as media_settings


try:
    from exiftool import ExifTool
except ImportError:
    EXIFTOOL = False
else:
    EXIFTOOL = True

USE_EXIFTOOL = EXIFTOOL and getattr(settings, 'MEDIASOURCES_USE_EXIFTOOL',
                                    True)


# Deprecated settings - moved to thecut.media.

CELERY = media_settings.CELERY

STATIC_ROOT = media_settings.STATIC_ROOT

STATICFILES_STORAGE = media_settings.STATICFILES_STORAGE

PLACEHOLDER_IMAGE_PATH = media_settings.PLACEHOLDER_IMAGE_PATH


# Deprecated settings - no longer in use.

GENERATE_THUMBNAILS_ON_SAVE = media_settings.QUEUE_THUMBNAILS

IMAGE_THUMBNAILS = ADMIN_IMAGE_THUMBNAILS = []

DOCUMENT_THUMBNAILS = ADMIN_DOCUMENT_THUMBNAILS = []

VIDEO_THUMBNAILS = ADMIN_VIDEO_THUMBNAILS = []

YOUTUBE_VIDEO_THUMBNAILS = []

VIMEO_VIDEO_THUMBNAILS = []
