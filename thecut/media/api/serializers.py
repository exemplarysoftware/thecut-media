# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from ..models import MediaContentType
from rest_framework import serializers
from rest_framework.reverse import reverse


class ContentTypeSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.Field(source='pk')

    url = serializers.HyperlinkedIdentityField(
        view_name='admin:media_api:contenttype_detail',
        lookup_field='pk')

    objects = serializers.SerializerMethodField('get_objects_url')

    verbose_name = serializers.SerializerMethodField('get_verbose_name')

    verbose_name_plural = serializers.SerializerMethodField(
        'get_verbose_name_plural')

    class Meta(object):
        fields = ['id',  'url', 'verbose_name', 'verbose_name_plural',
                  'objects']
        model = MediaContentType

    def get_objects_url(self, content_type):
        return reverse('admin:media_api:contenttype_object_list',
                       kwargs={'contenttype_pk': content_type.pk},
                       request=self.context['request'],
                       format=self.context['format'])

    def get_verbose_name(self, content_type):
        return content_type.model_class()._meta.verbose_name.title()

    def get_verbose_name_plural(self, content_type):
        return content_type.model_class()._meta.verbose_name_plural.title()


class MediaSerializer(serializers.ModelSerializer):

    id = serializers.Field(source='pk')

    name = serializers.Field(source='__str__')

    url = serializers.SerializerMethodField('get_url')

    thumbnail = serializers.SerializerMethodField('get_thumbnail')

    class Meta(serializers.ModelSerializer.Meta):
        fields = ['id', 'url', 'name', 'thumbnail', 'created_at', 'updated_at']

    def get_content_type(self):
        return MediaContentType.objects.get_for_model(self.Meta.model)

    def get_thumbnail(self, obj):
        # TODO
        return obj.get_image().url

    def get_url(self, obj):
        return reverse('admin:media_api:contenttype_object_detail',
                       kwargs={'pk': obj.pk,
                               'contenttype_pk': self.get_content_type().pk},
                       request=self.context['request'],
                       format=self.context['format'])
