# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.contenttypes.models import ContentType
from django.db import models
from functools import partial
from thecut.media import utils


class AttachedMediaItemQuerySet(models.query.QuerySet):
    """Customised :py:class:`~django.db.models.db.query.QuerySet` for
    :py:class:`~thecut.media.models.AttachedMediaItem` model."""

    def __init__(self, *args, **kwargs):
        #print("AttachedMediaItemQuerySet __init__")
        for class_ in utils.get_media_source_models():
            plural_name = class_._meta.verbose_name_plural.replace(' ', '')
            content_type = ContentType.objects.get_for_model(class_)
            objects = partial(self.get_objects_for_content_type,
                              content_type=content_type)
            setattr(self, plural_name, objects)
        super(AttachedMediaItemQuerySet, self).__init__(*args, **kwargs)

    def get_objects_for_content_type(self, content_type):
        pks = self.filter(content_type=content_type).values_list('pk',
                                                                 flat=True)
        return content_type.model_class().objects.filter(
            attachments__pk__in=pks).order_by('attachments__order')

    def get_image(self):
        images = self.images()[:1]
        if images:
            return images[0].get_image()
