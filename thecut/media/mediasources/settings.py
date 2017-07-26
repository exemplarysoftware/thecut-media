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

MEDIASOURCES_MAGIC_BUFFER_SIZE = getattr(settings,
                                         'MEDIASOURCES_MAGIC_BUFFER_SIZE',
                                         5120)


QUEUE_THUMBNAILS = media_settings.QUEUE_THUMBNAILS
