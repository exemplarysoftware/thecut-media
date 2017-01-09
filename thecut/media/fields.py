# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models.fields.related import lazy_related_operation


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
        #super(MediaGenericRelation, self).contribute_to_class(cls, name, **kwargs)
        from django.contrib.contenttypes.fields import ReverseGenericManyToOneDescriptor


        class MediaReverseGenericManyToOneDescriptor(ReverseGenericManyToOneDescriptor):

            @property
            def related_manager_cls(self):
                ret = super(MediaReverseGenericManyToOneDescriptor, self).related_manager_cls
                #print("ret=",ret)
                #print("type(ret)=",type(ret))
                #print("dir(ret)=",dir(ret))
                ret.images = property(lambda self: self.get_queryset().images)
                ret.youtubevideos = property(lambda self: self.get_queryset().youtubevideos)
                return ret

        #setattr(cls, self.name, MediaReverseGenericManyToOneDescriptor(self.remote_field))

        kwargs['private_only'] = True
        super(GenericRelation, self).contribute_to_class(cls, name, **kwargs)
        self.model = cls
        setattr(cls, self.name, MediaReverseGenericManyToOneDescriptor(self.remote_field))

        # Add get_RELATED_order() and set_RELATED_order() to the model this
        # field belongs to, if the model on the other end of this relation
        # is ordered with respect to its corresponding GenericForeignKey.
        if not cls._meta.abstract:

            def make_generic_foreign_order_accessors(related_model, model):
                if self._is_matching_generic_foreign_key(model._meta.order_with_respect_to):
                    make_foreign_order_accessors(model, related_model)

            lazy_related_operation(make_generic_foreign_order_accessors, self.model, self.remote_field.model)




