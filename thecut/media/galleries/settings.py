# -*- coding: utf-8 -*-
from django.conf import settings


GALLERY_PAGINATE_BY = getattr(settings, 'GALLERIES_GALLERY_PAGINATE_BY', 10)
GALLERY_MEDIA_PAGINATE_BY = getattr(settings,
    'GALLERIES_GALLERY_MEDIA_PAGINATE_BY', 10)

