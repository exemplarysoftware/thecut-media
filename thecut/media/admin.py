# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import settings
from .api.urls import generate_urls as generate_api_urls
from .forms import AttachedMediaItemInlineForm
from .models import AttachedMediaItem
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

try:
    from django.urls import reverse
except ImportError:
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

    def _get_media_api_url_namespace(self):
        return 'media_api-{}-{}'.format(self.model._meta.app_label,
                                        self.model._meta.model_name)

    def change_view(self, *args, **kwargs):
        extra_context = kwargs.pop('extra_context', {})

        media_contenttypes_api_url = reverse(
            '{}:{}:contenttype_list'.format(
                self.admin_site.name, self._get_media_api_url_namespace()))
        extra_context.update(
            {'media_contenttypes_api_url': media_contenttypes_api_url})

        kwargs.update({'extra_context': extra_context})
        return super(AttachedMediaItemMixin, self).change_view(*args, **kwargs)

    def get_urls(self, *args, **kwargs):
        media_api_urls = generate_api_urls(
            admin_site_name=self.admin_site.name,
            namespace=self._get_media_api_url_namespace(),
            media_models=self.attached_media_models)
        urlpatterns = [url(r'^media/api/', include(media_api_urls))]
        urlpatterns += super(AttachedMediaItemMixin, self).get_urls(*args,
                                                                    **kwargs)
        return urlpatterns
