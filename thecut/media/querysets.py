# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from functools import partial

from django.contrib.contenttypes.models import ContentType
from django.db import models
from thecut.media import utils


class AttachedMediaItemQuerySet(models.query.QuerySet):
    """Customised :py:class:`~django.db.models.db.query.QuerySet` for
    :py:class:`~thecut.media.models.AttachedMediaItem` model."""

    def __init__(self, *args, **kwargs):
        for class_ in utils.get_media_source_models():
            plural_name = class_._meta.verbose_name_plural.replace(' ', '')
            content_type = ContentType.objects.get_for_model(class_)
            objects = partial(self.get_objects_for_content_type,
                              content_type=content_type)
            setattr(self, plural_name, objects)
            attr = getattr(self, plural_name)
            attr.generated_mediaitemqueryset_method = True
        super(AttachedMediaItemQuerySet, self).__init__(*args, **kwargs)

    def get_objects_for_content_type(self, content_type):
        return content_type.model_class().objects.filter(
            attachments__in=self.filter(content_type=content_type)).order_by(
            'attachments__order')

    def get_image(self):
        image = self.images().first()
        if image:
            return image.get_image()
