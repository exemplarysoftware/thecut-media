# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import settings
from .api.urls import generate_urls as generate_api_urls
from .forms import AttachedMediaItemInlineForm
from .models import AttachedMediaItem
from django.conf.urls import include
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from django.conf.urls import url
from .utils import show_urls
from django import get_version as get_django_version
from django.core.urlresolvers import reverse


class AttachedMediaItemInline(GenericStackedInline):

    ct_field = 'parent_content_type'

    ct_fk_field = 'parent_object_id'

    extra = 0

    form = AttachedMediaItemInlineForm

    model = AttachedMediaItem

    template = 'media/admin/media/_attachedmediaitem_inline.html'

    verbose_name_plural = 'Attached Media'


class AttachedMediaItemMixin(admin.ModelAdmin):

    inlines = [AttachedMediaItemInline]

    attached_media_models = settings.DEFAULT_ATTACHED_MEDIA_MODELS

    def get_urls(self):
        media_api_namespace = 'media_api-{0}-{1}'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        media_api_urls = generate_api_urls(
            admin_site_name=self.admin_site.name,
            namespace=media_api_namespace,
            media_models=self.attached_media_models)
        #print("self.attached_media_models=",self.attached_media_models)
        print("AttachedMediaItemMixin self.admin_site.name=",self.admin_site.name)
        print("AttachedMediaItemMixin media_api_namespace=",media_api_namespace)
        print("Contenttypes url = ", reverse(self.admin_site.name + ":" + media_api_namespace + ":contenttype_list"))
        urlpatterns = [
            url(r'^media/api/', include(media_api_urls)),
        ]
        urlpatterns += super(AttachedMediaItemMixin, self).get_urls()

        #show_urls(urlpatterns)
        return urlpatterns

    def change_view(self, request, object_id, form_url='', extra_context=None):
        #print('AttachedMediaItemMixin change_view called')
        version = get_django_version().split('.')
        assert len(version) == 3
        assert version[0] == '1' # Unknown django version
        extra_context = extra_context or {}
        if version[1] == '8':
            data_api_href = '../media/api/contenttypes/'
        elif version[1] == '9' or version[1] == '10':
            data_api_href = '../../media/api/contenttypes/'
        else:
            assert False # Unknown version number
        extra_context['data_api_href'] = data_api_href
        return super(AttachedMediaItemMixin, self).change_view(request, object_id, form_url, extra_context)

