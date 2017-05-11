# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def delete_media_attachments(sender, instance, **kwargs):
    """Delete attachments when media item is deleted."""
    from django.contrib.contenttypes.models import ContentType
    from thecut.media.models import AbstractMediaItem, AttachedMediaItem
    if issubclass(instance.__class__, AbstractMediaItem):
        content_type = ContentType.objects.get_for_model(sender)
        attachments = AttachedMediaItem.objects.filter(
            content_type=content_type, object_id=instance.pk)
        attachments.delete()


def add_media_generic_relation(sender, **kwargs):
    from django.contrib.contenttypes.fields import GenericRelation
    from thecut.publishing.models import Content
    if issubclass(sender, Content):
        sender.add_to_class(
            'media',
            GenericRelation('media.AttachedMediaItem',
                            content_type_field='parent_content_type',
                            object_id_field='parent_object_id')
        )
