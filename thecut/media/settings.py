# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf import settings
from sorl.thumbnail.conf import settings as sorl_settings


DEBUG = getattr(settings, 'MEDIA_DEBUG', settings.DEBUG)

MEDIA_PAGINATE_BY = getattr(settings, 'MEDIA_PAGINATE_BY', 7)

MEDIA_SOURCES = getattr(settings, 'MEDIA_SOURCES', [])


# Thumbnail / placeholder settings

CELERY = 'djcelery' in settings.INSTALLED_APPS

PLACEHOLDER_IMAGE_PATH = getattr(
    settings, 'MEDIA_PLACEHOLDER_IMAGE_PATH',
    # Also check old setting name
    getattr(settings, 'MEDIASOURCES_PLACEHOLDER_IMAGE_PATH',
    'media/placeholder.{0}'.format('svg' if not 'pil_engine' in
                                   sorl_settings.THUMBNAIL_ENGINE else 'png')))

QUEUE_THUMBNAILS = CELERY and getattr(
    settings, 'MEDIA_QUEUE_THUMBNAILS',
    # Also check old setting name
    getattr(settings, 'MEDIASOURCES_GENERATE_THUMBNAILS_ON_SAVE', not DEBUG))

ADMIN_THUMBNAIL_SIZES = getattr(
    settings, 'MEDIA_ADMIN_THUMBNAIL_SIZES', [
    # List of tuples containing geometry_size and options dict
    ('60x45', {'crop': 'center'}),
    ('100x75', {}),
    ('140x106', {'crop': 'center'}),
])

PREGENERATE_THUMBNAIL_SIZES = ADMIN_THUMBNAIL_SIZES + getattr(
    settings, 'MEDIA_PREGENERATE_THUMBNAIL_SIZES', [])

STATIC_ROOT = getattr(settings, 'STATIC_ROOT', settings.MEDIA_ROOT)

STATICFILES_STORAGE = getattr(settings, 'STATICFILES_STORAGE', False)
