# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.contenttypes.fields import GenericRelation


try:
    from django.contrib.contenttypes.fields import GenericForeignKey
except ImportError:  # pre Django 1.7 compatibility
    from django.contrib.contenttypes.generic import GenericForeignKey


class MediaForeignKey(GenericForeignKey):

    def _check_content_type_field(self):
        # TODO Custom check for MediaContentType?
        return []

    def get_content_type(self, *args, **kwargs):
        from .models import MediaContentType
        content_type = super(MediaForeignKey, self).get_content_type(*args,
                                                                     **kwargs)
        return MediaContentType.objects.get(pk=content_type.pk)


class MediaGenericRelation(GenericRelation):
    def contribute_to_class(self, cls, name, **kwargs):
        super(MediaGenericRelation, self).contribute_to_class(cls, name, **kwargs)
        from django.contrib.contenttypes.fields import ReverseGenericManyToOneDescriptor


        class MediaReverseGenericManyToOneDescriptor(ReverseGenericManyToOneDescriptor):

            @property
            def related_manager_cls(self):
                ret = super(MediaReverseGenericManyToOneDescriptor, self).related_manager_cls()
                ret.images = lambda self: self.get_queryset().images
                return ret

        setattr(cls, self.name, MediaReverseGenericManyToOneDescriptor(self.remote_field))



