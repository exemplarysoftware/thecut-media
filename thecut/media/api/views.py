# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import permissions, serializers
from ..models import MediaContentType
from rest_framework import authentication, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class APIMixin(object):

    authentication_classes = [authentication.SessionAuthentication]

    paginate_by = 10

    paginate_by_param = 'limit'

    max_paginate_by = 100

    permission_classes = [permissions.IsAdminUser]


class MediaRootAPIView(APIMixin, APIView):

    def get(self, request, format=None):
        return Response(
            {'contentttypes': reverse('admin:media_api:contenttype_list',
                                      request=request)})


class ContentTypeListAPIView(APIMixin, generics.ListAPIView):

    model = MediaContentType

    permission_classes = APIMixin.permission_classes + [
        permissions.MediaPermissions]

    serializer_class = serializers.ContentTypeSerializer


class ContentTypeRetrieveAPIView(APIMixin, generics.RetrieveAPIView):

    model = MediaContentType

    permission_classes = APIMixin.permission_classes + [
        permissions.MediaPermissions]

    serializer_class = serializers.ContentTypeSerializer


class ContentTypeObjectListAPIView(APIMixin, generics.ListAPIView):

    permission_classes = APIMixin.permission_classes + [
        permissions.MediaPermissions]

    serializer_class = serializers.MediaSerializer

    def get_content_type(self):
        return generics.get_object_or_404(MediaContentType,
                                          pk=self.kwargs.get('contenttype_pk'))

    def initial(self, *args, **kwargs):
        # Model needs to be set on the class for permission checks
        self.model = self.get_model()
        return super(ContentTypeObjectListAPIView, self).initial(*args,
                                                                 **kwargs)

    def get_model(self):
        return self.get_content_type().model_class()

    def get_serializer_class(self):
        # Set ``model`` on a new serializer class

        class Serializer(self.serializer_class):
            class Meta(self.serializer_class.Meta):
                model = self.model

        return Serializer

    def get_view_name(self, *args, **kwargs):
        view_name = super(ContentTypeObjectListAPIView, self).get_view_name(
            *args, **kwargs)
        return '{0} ({1})'.format(
            view_name, self.get_model()._meta.verbose_name_plural.title())
