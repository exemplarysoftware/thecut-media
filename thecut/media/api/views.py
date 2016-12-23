# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import forms, pagination, permissions, serializers
from ..models import MediaContentType
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from rest_framework import authentication, generics, renderers, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class APIMixin(object):

    authentication_classes = [authentication.SessionAuthentication]

    pagination_class = pagination.DefaultPagination

    permission_classes = [permissions.IsAdminUser]

    renderer_classes = [renderers.JSONRenderer]

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(APIMixin, self).dispatch(*args, **kwargs)


class MediaRootAPIView(APIMixin, APIView):

    def get(self, request, url_namespace, format=None):
        contenttype_list_url = reverse(
            '{0}:contenttype_list'.format(url_namespace), request=request)
        return Response(
            {'contentttypes': contenttype_list_url})


class BaseContentTypeAPIMixin(APIMixin):

    permission_classes = APIMixin.permission_classes + [
        permissions.MediaPermissions]

    queryset = MediaContentType.objects.all()

    serializer_class = serializers.ContentTypeSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = super(BaseContentTypeAPIMixin, self).get_queryset(*args,
                                                                     **kwargs)
        media_models = self.kwargs['media_models']
        if media_models:
            queryset = MediaContentType.objects.get_for_models(media_models)
        print("BaseContentTypeAPIMixin media_models=",media_models)
        print("BaseContentTypeAPIMixin list(queryset)=",list(queryset))
        return queryset

    def get_serializer_context(self, *args, **kwargs):
        context = super(BaseContentTypeAPIMixin, self).get_serializer_context(
            *args, **kwargs)
        context.update({'media_models': self.kwargs['media_models']})
        return context


class ContentTypeListAPIView(BaseContentTypeAPIMixin, generics.ListAPIView):

    pass


class ContentTypeRetrieveAPIView(BaseContentTypeAPIMixin,
                                 generics.RetrieveAPIView):

    pass


class BaseContentTypeObjectAPIMixin(APIMixin):

    permission_classes = APIMixin.permission_classes + [
        permissions.MediaPermissions]

    serializer_class = serializers.MediaSerializer

    def get_content_type(self):
        media_models = self.kwargs['media_models']
        if media_models:
            queryset = MediaContentType.objects.get_for_models(media_models)
        else:
            queryset = MediaContentType
        return generics.get_object_or_404(queryset,
                                          pk=self.kwargs.get('contenttype_pk'))

    def initial(self, *args, **kwargs):
        # Queryset needs to be set on the class for permission checks
        self.queryset = self.get_model().objects.all()
        return super(BaseContentTypeObjectAPIMixin, self).initial(*args,
                                                                  **kwargs)

    def get_model(self):
        return self.get_content_type().model_class()

    def get_serializer_class(self):
        # Set ``model`` on a new serializer class

        class Serializer(self.serializer_class):
            class Meta(self.serializer_class.Meta):
                model = self.queryset.model

        return Serializer

    def get_view_name(self, *args, **kwargs):
        view_name = super(BaseContentTypeObjectAPIMixin, self).get_view_name(
            *args, **kwargs)
        return '{0} ({1})'.format(
            view_name, self.get_model()._meta.verbose_name_plural.title())


class ContentTypeObjectListAPIView(BaseContentTypeObjectAPIMixin,
                                   generics.ListAPIView):

    form_class = forms.FilterForm

    pagination_class = pagination.TaggedPagination

    def get_form(self):
        return self.form_class(data=self.get_form_data())

    def get_form_data(self):
        return {
            'q': self.request.query_params.get('q'),
            # TODO: Can we just make the form accept a list of values?
            'tags': ','.join(self.request.query_params.getlist('tag', ''))
        }

    def get_queryset(self, *args, **kwargs):
        queryset = super(ContentTypeObjectListAPIView, self).get_queryset(
            *args, **kwargs)
        return self.get_form().filter_queryset(queryset)

    def list(self, request, *args, **kwargs):
        self.form = self.get_form()
        if not self.form.is_valid():
            return Response(self.form.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        return super(ContentTypeObjectListAPIView, self).list(request, *args,
                                                              **kwargs)


class ContentTypeObjectDetailAPIView(BaseContentTypeObjectAPIMixin,
                                     generics.RetrieveAPIView):

    pass
