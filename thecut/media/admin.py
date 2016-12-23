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
        print("self.attached_media_models=",self.attached_media_models)
        urlpatterns = [
            url(r'^media/api/', include(media_api_urls)),
        ]
        urlpatterns += super(AttachedMediaItemMixin, self).get_urls()

        show_urls(urlpatterns)
        return urlpatterns
