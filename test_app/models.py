# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
import uuid
from thecut.media.fields import MediaGenericRelation


class MediaTestModel(models.Model):
    media = MediaGenericRelation('media.AttachedMediaItem',
                                 content_type_field='parent_content_type',
                                 object_id_field='parent_object_id')


class MediaTestUUIDPKModel(models.Model):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4,
                          editable=False)

    media = MediaGenericRelation('media.AttachedMediaItem',
                                 content_type_field='parent_content_type',
                                 object_id_field='parent_object_id')
