# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .utils import get_media_source_models
from django.contrib.contenttypes.models import ContentTypeManager
from django.db.models import Q
import operator


class MediaContentTypeManager(ContentTypeManager):

    _queryset = None

    def get_queryset(self, *args, **kwargs):
        queryset = super(MediaContentTypeManager, self).get_query_set(*args,
                                                                      **kwargs)

        # Evaluate the queryset and store it on the class
        if MediaContentTypeManager._queryset is None:
            models = get_media_source_models()
            query = reduce(operator.or_, (Q(app_label=model._meta.app_label,
                                            model=model._meta.model_name)
                                          for model in models))
            queryset = queryset.filter(query)
            bool(queryset)  # Force evaluation
            MediaContentTypeManager._queryset = queryset

        return MediaContentTypeManager._queryset