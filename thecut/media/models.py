# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.contenttypes import generic
from django.db import models
from model_utils.managers import PassThroughManager
from tagging.fields import TagField
from thecut.media import querysets, receivers
from thecut.ordering.models import OrderMixin
from thecut.publishing.models import PublishableResource, Content
from thecut.publishing.utils import python_2_unicode_compatible


@python_2_unicode_compatible
class AbstractMediaItem(PublishableResource):

    title = models.CharField(max_length=200, db_index=True)
    caption = models.TextField(blank=True, default='')
    content = models.TextField(blank=True, default='')
    tags = TagField(blank=True, default='',
                    help_text='Separate tags with spaces, put quotes around '
                              'multiple-word tags.')
    attachments = generic.GenericRelation('media.AttachedMediaItem',
                                          content_type_field='content_type',
                                          object_id_field='object_id')

    class Meta(PublishableResource.Meta):
        abstract = True

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class AttachedMediaItem(OrderMixin, models.Model):

    # Generic relation to media object.
    content_type = models.ForeignKey('contenttypes.ContentType')
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    # Generic relation to another object.
    parent_content_type = models.ForeignKey(
        'contenttypes.ContentType',
        related_name='attachedmediaitem_parent_set')
    parent_object_id = models.IntegerField(db_index=True)
    parent_content_object = generic.GenericForeignKey('parent_content_type',
                                                      'parent_object_id')

    objects = PassThroughManager().for_queryset_class(
        querysets.AttachedMediaItemQuerySet)()

    def __str__(self):
        return '{0} - {1}: {2}'.format(self.order, self.content_type,
                                       self.content_object)


# Let's be helpful, and add media generic relation field to Content model.
Content.add_to_class(
    'media',
    generic.GenericRelation('media.AttachedMediaItem',
                            content_type_field='parent_content_type',
                            object_id_field='parent_object_id')
)

models.signals.pre_delete.connect(receivers.delete_media_attachments)
