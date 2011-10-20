# -*- coding: utf-8 -*-
from django.coding import settings


DEBUG = settings.DEBUG
MEDIA_PAGINATE_BY = getattr(settings, 'MEDIA_PAGINATE_BY', 7)
MEDIA_SOURCES = getattr(settings, 'MEDIA_SOURCES', [])

