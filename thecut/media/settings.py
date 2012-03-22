# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf import settings


DEBUG = settings.DEBUG
MEDIA_PAGINATE_BY = getattr(settings, 'MEDIA_PAGINATE_BY', 7)
MEDIA_SOURCES = getattr(settings, 'MEDIA_SOURCES', [])

