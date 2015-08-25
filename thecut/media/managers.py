# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .utils import get_media_source_models
from django.contrib.contenttypes.models import ContentTypeManager
from django.db.models import Model, Q
import operator


class MediaContentTypeManager(ContentTypeManager):

    _media_queryset = None

    def get_for_models(self, models):
        q_args = []
        for model in models:
            if isinstance(model, basestring):
                app_label = model.split('.')[0]
                model_name = '.'.join(model.split('.')[1:])
                q_args += [(app_label, model_name)]
            elif issubclass(model, Model):
                q_args += [(model._meta.app_label, model._meta.model_name)]
        query = reduce(operator.or_, (Q(app_label__iexact=app_label,
                                        model__iexact=model)
                                      for app_label, model in q_args))
        return self.filter(query)

    def get_queryset(self, *args, **kwargs):
        queryset = super(MediaContentTypeManager, self).get_queryset(*args,
                                                                     **kwargs)

        # Evaluate the queryset and store it on the class
        if MediaContentTypeManager._media_queryset is None:
            models = get_media_source_models()
            query = reduce(operator.or_, (Q(app_label=model._meta.app_label,
                                            model=model._meta.model_name)
                                          for model in models))
            queryset = queryset.filter(query)
            MediaContentTypeManager._media_queryset = queryset

        return MediaContentTypeManager._media_queryset
