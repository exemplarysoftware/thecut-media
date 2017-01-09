# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import fields, managers, querysets, receivers
#from django.contrib.contenttypes import generic
from django.contrib.contenttypes.fields import (GenericRelation,
                                                GenericForeignKey)
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
#from model_utils.managers import PassThroughManager
from taggit.managers import TaggableManager
from thecut.ordering.models import OrderMixin
from thecut.publishing.models import PublishableResource
import django


@python_2_unicode_compatible
class MediaContentType(ContentType):

    objects = managers.MediaContentTypeManager()

    class Meta(object):
        proxy = True

    def __str__(self):
        return self.name.title()


@python_2_unicode_compatible
class AbstractMediaItem(PublishableResource):

    title = models.CharField(max_length=200, db_index=True)

    caption = models.TextField(blank=True, default='')

    content = models.TextField(blank=True, default='')

    if django.VERSION < (1, 7):
        tags = TaggableManager(blank=True)
    else:
        tags = TaggableManager(blank=True, related_name='+')

    attachments = GenericRelation('media.AttachedMediaItem',
                                  content_type_field='content_type',
                                  object_id_field='object_id')

    class Meta(PublishableResource.Meta):
        abstract = True
        ordering = ['-created_at']

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return self.title


@python_2_unicode_compatible
class AttachedMediaItem(OrderMixin, models.Model):

    # Generic relation to media object.
    content_type = models.ForeignKey(
        'media.MediaContentType', related_name='+', on_delete=models.CASCADE)
    object_id = models.IntegerField(db_index=True)
    content_object = fields.MediaForeignKey('content_type', 'object_id')

    # Generic relation to another object.
    parent_content_type = models.ForeignKey(
        'contenttypes.ContentType',
        related_name='attachedmediaitem_parent_set', on_delete=models.CASCADE)
    parent_object_id = models.IntegerField(db_index=True)
    parent_content_object = GenericForeignKey('parent_content_type',
                                              'parent_object_id')

    #objects = PassThroughManager().for_queryset_class(
    #    querysets.AttachedMediaItemQuerySet)()
    objects = querysets.AttachedMediaItemQuerySet.as_manager()

    def __str__(self):
        return '{0} - {1}: {2}'.format(self.order, self.content_type,
                                       self.content_object)

models.signals.pre_delete.connect(receivers.delete_media_attachments)


# Let's be helpful, and add media generic relation field to anything that
# extends the Content model.
models.signals.class_prepared.connect(receivers.add_media_generic_relation)
