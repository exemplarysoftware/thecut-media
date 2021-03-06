# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from collections import OrderedDict

from rest_framework import serializers
from rest_framework.reverse import reverse

from .. import utils
from ..mediasources.models import FileMixin
from ..mediasources.settings import USE_S3UPLOAD
from ..models import MediaContentType

try:
    from django.urls import NoReverseMatch
except ImportError:
    from django.core.urlresolvers import NoReverseMatch


class BaseFileUpload(object):

    file_parameter = 'file'

    def __init__(self, content_type, request):
        self.content_type = content_type
        self.request = request

    def can_upload_files(self):
        has_file = issubclass(self.content_type.model_class(), FileMixin)
        has_permission = self.request.user.has_perm(
            '{0}.add_{1}'.format(self.content_type.app_label,
                                 self.content_type.model))
        return has_file and has_permission

    def properties(self):
        if self.can_upload_files():
            return {'url': self.get_url(),
                    'data': self.get_form_data(),
                    'file_parameter': self.get_file_parameter(),
                    'notify_url': self.get_notify_url(),
                    'notify_data': self.get_notify_data()}

    def get_form_data(self):
        form = self.get_form()
        data = OrderedDict()
        for field in form.fields:
            field_name = form.add_prefix(field)
            initial_data = form.fields[field].initial
            if initial_data:
                data.update({field_name: form.fields[field].initial})
        return data

    def get_file_parameter(self):
        return self.file_parameter

    def get_form(self):
        raise NotImplementedError()

    def get_url(self):
        raise NotImplementedError()

    def get_notify_data(self):
        return {}

    def get_notify_url(self):
        return None


class MediaFileUpload(BaseFileUpload):

    file_parameter = 'files'

    def get_form_data(self, *args, **kwargs):
        data = super(MediaFileUpload, self).get_form_data(*args, **kwargs)
        csrf_token = self.request.META.get('CSRF_COOKIE')
        data.update({'csrfmiddlewaretoken': csrf_token})
        return data

    def get_form(self):
        from thecut.media.mediasources.forms import MediaUploadForm
        return MediaUploadForm()

    def get_url(self):
        # TODO: We should process these files at an API url endpoint
        try:
            return reverse(
                'admin:{app_label}_{model_name}_add'.format(
                    app_label=self.content_type.app_label,
                    model_name=self.content_type.model))
        except NoReverseMatch:
            pass


class DropzoneFileUpload(BaseFileUpload):

    def get_form(self):
        from s3upload.forms import DropzoneS3UploadForm
        return DropzoneS3UploadForm()

    def get_url(self):
        return self.get_form().get_action()

    def get_notify_data(self, *args, **kwargs):
        data = super(DropzoneFileUpload, self).get_notify_data(*args, **kwargs)
        csrf_token = self.request.META.get('CSRF_COOKIE')
        data.update({'csrfmiddlewaretoken': csrf_token})
        return data

    def get_notify_url(self):
        # TODO: We should process these files at an API url endpoint
        try:
            return reverse(
                'admin:{app_label}_{model_name}_add'.format(
                    app_label=self.content_type.app_label,
                    model_name=self.content_type.model))
        except NoReverseMatch:
            pass


class ContentTypeSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.ReadOnlyField(source='pk')

    url = serializers.SerializerMethodField()

    objects = serializers.SerializerMethodField('get_objects_url')

    verbose_name = serializers.SerializerMethodField()

    verbose_name_plural = serializers.SerializerMethodField()

    file_upload = serializers.SerializerMethodField()

    order = serializers.SerializerMethodField()

    class Meta(object):
        fields = ['url', 'id', 'verbose_name', 'verbose_name_plural',
                  'objects', 'file_upload', 'order']
        model = MediaContentType

    def get_file_upload(self, content_type):
        kwargs = {'content_type': content_type,
                  'request': self.context['request']}
        if USE_S3UPLOAD:
            file_upload = DropzoneFileUpload(**kwargs)
        else:
            file_upload = MediaFileUpload(**kwargs)
        return file_upload.properties()

    def get_objects_url(self, content_type):
        namespace = self.context['view'].kwargs['url_namespace']
        return reverse('{0}:contenttype_object_list'.format(namespace),
                       kwargs={'contenttype_pk': content_type.pk},
                       request=self.context['request'],
                       format=self.context['format'])

    def get_url(self, content_type):
        namespace = self.context['view'].kwargs['url_namespace']
        return reverse('{0}:contenttype_detail'.format(namespace),
                       kwargs={'pk': content_type.pk},
                       request=self.context['request'],
                       format=self.context['format'])

    def get_verbose_name(self, content_type):
        return content_type.model_class()._meta.verbose_name.title()

    def get_verbose_name_plural(self, content_type):
        return content_type.model_class()._meta.verbose_name_plural.title()

    def get_order(self, content_type):
        # Content Types should retain the order in which they are
        # defined in the settings.
        models = [self._get_app_model(model)
                  for model in self.context['media_models']]
        content_type_model = (content_type.app_label, content_type.model)
        return models.index(content_type_model)

    def _get_app_model(self, content_type):
        # Given a string like 'app_label.ModelName', return a 2-tuple
        # consisting of ('app_label', 'modelname')
        app_label, model_name = content_type.lower().split('.')
        return (app_label, model_name)


class MediaSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField(source='pk')

    name = serializers.ReadOnlyField(source='get_name')

    url = serializers.SerializerMethodField()

    thumbnail = serializers.SerializerMethodField()

    class Meta(object):
        fields = ['url', 'id', 'name', 'thumbnail', 'created_at', 'updated_at']

    def get_content_type(self):
        return MediaContentType.objects.get_for_model(self.Meta.model)

    def get_thumbnail(self, obj):
        if hasattr(obj, 'get_image'):
            try:
                return utils.get_preview_thumbnail(obj.get_image()).url
            except:
                pass

    def get_url(self, obj):
        namespace = self.context['view'].kwargs['url_namespace']
        return reverse('{0}:contenttype_object_detail'.format(namespace),
                       kwargs={'pk': obj.pk,
                               'contenttype_pk': self.get_content_type().pk},
                       request=self.context['request'],
                       format=self.context['format'])
