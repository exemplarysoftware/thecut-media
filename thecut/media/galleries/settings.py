# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf import settings


GALLERY_PAGINATE_BY = getattr(settings, 'GALLERIES_GALLERY_PAGINATE_BY', 10)

GALLERY_MEDIA_PAGINATE_BY = getattr(settings,
                                    'GALLERIES_GALLERY_MEDIA_PAGINATE_BY', 10)
