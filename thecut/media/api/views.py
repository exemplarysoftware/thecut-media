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
