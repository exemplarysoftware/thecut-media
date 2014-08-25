# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf import settings
from sorl.thumbnail.conf import settings as sorl_settings


DEBUG = getattr(settings, 'MEDIA_DEBUG', settings.DEBUG)


DEFAULT_ATTACHED_MEDIA_MODELS = getattr(
    settings, 'MEDIA_DEFAULT_ATTACHED_MEDIA_MODELS', None)


# Thumbnail / placeholder settings

try:
    from celery import Celery
    CELERY = True
except ImportError:
    CELERY = False

PLACEHOLDER_IMAGE_PATH = getattr(
    settings, 'MEDIA_PLACEHOLDER_IMAGE_PATH',
    # Also check old setting name
    getattr(
        settings, 'MEDIASOURCES_PLACEHOLDER_IMAGE_PATH',
        'media/placeholder.{0}'.format('svg' if 'pil_engine' not in
                                       sorl_settings.THUMBNAIL_ENGINE
                                       else 'png')))

QUEUE_THUMBNAILS = CELERY and getattr(
    settings, 'MEDIA_QUEUE_THUMBNAILS',
    # Also check old setting name
    getattr(settings, 'MEDIASOURCES_GENERATE_THUMBNAILS_ON_SAVE', not DEBUG))

ADMIN_THUMBNAIL_SIZES = getattr(
    settings, 'MEDIA_ADMIN_THUMBNAIL_SIZES', [
        # List of tuples containing geometry_size and options dict
        ('360x360', {'quality': 50}),
    ])

PREGENERATE_THUMBNAIL_SIZES = ADMIN_THUMBNAIL_SIZES + getattr(
    settings, 'MEDIA_PREGENERATE_THUMBNAIL_SIZES', [])

STATIC_ROOT = getattr(settings, 'STATIC_ROOT', settings.MEDIA_ROOT)

STATICFILES_STORAGE = getattr(settings, 'STATICFILES_STORAGE', False)
