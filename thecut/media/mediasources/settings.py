# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf import settings
from thecut.media import settings as media_settings


try:
    from exiftool import ExifTool
except ImportError:
    ExifTool = False


USE_S3UPLOAD = 's3upload' in settings.INSTALLED_APPS and getattr(
    settings, 'MEDIASOURCES_USE_S3UPLOAD', True)


USE_EXIFTOOL = ExifTool and getattr(settings, 'MEDIASOURCES_USE_EXIFTOOL',
                                    True)

MEDIASOURCES_MAGIC_BUFFER_SIZE = 5120


QUEUE_THUMBNAILS = media_settings.QUEUE_THUMBNAILS


# Deprecated settings - moved to thecut.media.

CELERY = media_settings.CELERY

STATIC_ROOT = media_settings.STATIC_ROOT

STATICFILES_STORAGE = media_settings.STATICFILES_STORAGE

PLACEHOLDER_IMAGE_PATH = media_settings.PLACEHOLDER_IMAGE_PATH


# Deprecated settings - no longer in use.

GENERATE_THUMBNAILS_ON_SAVE = media_settings.QUEUE_THUMBNAILS

ADMIN_IMAGE_THUMBNAILS = media_settings.PREGENERATE_THUMBNAIL_SIZES

IMAGE_THUMBNAILS = media_settings.PREGENERATE_THUMBNAIL_SIZES

ADMIN_DOCUMENT_THUMBNAILS = media_settings.PREGENERATE_THUMBNAIL_SIZES

DOCUMENT_THUMBNAILS = media_settings.PREGENERATE_THUMBNAIL_SIZES

ADMIN_VIDEO_THUMBNAILS = media_settings.PREGENERATE_THUMBNAIL_SIZES

VIDEO_THUMBNAILS = media_settings.PREGENERATE_THUMBNAIL_SIZES

YOUTUBE_VIDEO_THUMBNAILS = media_settings.PREGENERATE_THUMBNAIL_SIZES

VIMEO_VIDEO_THUMBNAILS = media_settings.PREGENERATE_THUMBNAIL_SIZES
