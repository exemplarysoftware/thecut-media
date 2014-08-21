# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .. import utils
from ..mediasources.models import FileMixin
from ..mediasources.settings import USE_S3UPLOAD
from ..models import MediaContentType
from django.core.urlresolvers import NoReverseMatch
from django.utils.datastructures import SortedDict
from rest_framework import pagination, serializers
from rest_framework.reverse import reverse
from taggit.models import Tag


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
        data = SortedDict()
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

    id = serializers.Field(source='pk')

    url = serializers.HyperlinkedIdentityField(
        view_name='admin:media_api:contenttype_detail',
        lookup_field='pk')

    objects = serializers.SerializerMethodField('get_objects_url')

    verbose_name = serializers.SerializerMethodField('get_verbose_name')

    verbose_name_plural = serializers.SerializerMethodField(
        'get_verbose_name_plural')

    file_upload = serializers.SerializerMethodField(
        'get_file_upload')

    class Meta(object):
        fields = ['id',  'url', 'verbose_name', 'verbose_name_plural',
                  'objects', 'file_upload']
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
        if hasattr(obj, 'get_image'):
            try:
                return utils.get_preview_thumbnail(obj.get_image()).url
            except:
                pass

    def get_url(self, obj):
        return reverse('admin:media_api:contenttype_object_detail',
                       kwargs={'pk': obj.pk,
                               'contenttype_pk': self.get_content_type().pk},
                       request=self.context['request'],
                       format=self.context['format'])


class PaginationSerializerWithTags(pagination.PaginationSerializer):

    tags = serializers.SerializerMethodField('get_tags')

    def get_tags(self, page):
        queryset = page.paginator.object_list
        model_name = queryset.model._meta.model_name
        filters = {'{0}__pk__in'.format(model_name): queryset}
        return Tag.objects.filter(**filters).distinct().values_list(
            'name', flat=True)
