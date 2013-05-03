# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from distutils.version import StrictVersion
from django import get_version
from django.contrib.auth.decorators import user_passes_test
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from tagging.models import Tag, TaggedItem
from thecut.media import settings, MEDIA_SOURCE_CLASSES
from thecut.media.forms import MediaSearchForm

if StrictVersion(get_version()) < StrictVersion('1.3'):
    # Pre-Django 1.3 compatibility
    import cbv as generic
else:
    from django.views import generic


class AdminContentTypeList(generic.TemplateView):

    template_name = 'media/_contenttype_list.html'

    @method_decorator(never_cache)
    @method_decorator(user_passes_test(
        lambda u:
            u.has_perm('media.add_attachedmediaitem') or
            u.has_perm('media.change_attachedmediaitem')))
    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax() or settings.DEBUG:
            return super(AdminContentTypeList, self).dispatch(
                request, *args, **kwargs)
        else:
            return HttpResponseBadRequest(content_type='text/plain')

    def get_content_types(self):
        return [ContentType.objects.get_for_model(model) for model in
                MEDIA_SOURCE_CLASSES]

    def get_context_data(self, *args, **kwargs):
        context_data = super(AdminContentTypeList, self).get_context_data(
            *args, **kwargs)
        context_data.update({'content_type_list': self.get_content_types()})
        return context_data


class AdminContentTypeObjectList(generic.ListView):

    paginate_by = settings.MEDIA_PAGINATE_BY

    @method_decorator(never_cache)
    @method_decorator(user_passes_test(
        lambda u: u.has_perm('media.add_attachedmediaitem') or
                  u.has_perm('media.change_attachedmediaitem')))
    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax() or settings.DEBUG:
            return super(AdminContentTypeObjectList, self).dispatch(
                request, *args, **kwargs)
        else:
            return HttpResponseBadRequest(content_type='text/plain')

    def get_content_type(self):
        if not hasattr(self, '_content_type'):
            self._content_type = get_object_or_404(
                ContentType, pk=self.kwargs.get('content_type_pk'))
        return self._content_type

    def get_context_data(self, *args, **kwargs):
        context_data = super(AdminContentTypeObjectList,
                             self).get_context_data(*args, **kwargs)
        context_data.update({'content_type': self.get_content_type(),
                             'form': self.form})
        return context_data

    def get_form(self, tags):
        form = MediaSearchForm(tags, self.request.GET)
        form.is_valid()
        return form

    def get_model(self):
        if not hasattr(self, '_model'):
            self._model = self.get_content_type().model_class()
        return self._model

    def get_queryset(self):
        queryset = self.get_model().objects.active()

        tags = self.get_tags(queryset)
        form = self.get_form(tags)

        # If a search query has been made, filter queryset some more
        q = form.cleaned_data.get('q')
        if q:
            queryset = queryset.filter(title__icontains=q)

        # If tags have been selected, then filter queryset and form some more
        selected_tags = form.cleaned_data.get('tags')
        if selected_tags:
            queryset = TaggedItem.objects.get_intersection_by_model(
                queryset, Tag.objects.filter(pk__in=selected_tags))
            tags = self.get_tags(queryset)

        self.form = MediaSearchForm(
            tags, initial={'q': q, 'tags': selected_tags})

        return queryset

    def get_tags(self, queryset):
        return Tag.objects.usage_for_queryset(queryset, counts=True)

    def get_template_names(self, *args, **kwargs):
        return ['admin/{0}/{1}/_picker.html'.format(
                self.get_model()._meta.app_label,
                self.get_model()._meta.object_name.lower())]


class AdminContentTypeSelectedObjectList(generic.ListView):

    @method_decorator(never_cache)
    @method_decorator(user_passes_test(
        lambda u: u.has_perm('media.add_attachedmediaitem') or
                  u.has_perm('media.change_attachedmediaitem')))
    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax() or settings.DEBUG:
            return super(AdminContentTypeSelectedObjectList, self).dispatch(
                request, *args, **kwargs)
        else:
            return HttpResponseBadRequest(content_type='text/plain')

    def get_content_type(self):
        if not hasattr(self, '_content_type'):
            self._content_type = get_object_or_404(
                ContentType, pk=self.kwargs.get('content_type_pk'))
        return self._content_type

    def get_context_data(self, *args, **kwargs):
        context_data = super(AdminContentTypeSelectedObjectList,
                             self).get_context_data(*args, **kwargs)
        context_data.update({'content_type': self.get_content_type()})
        return context_data

    def get_context_object_name(self, object_list):
        return '{0}_list'.format(self.get_model()._meta.object_name.lower())

    def get_model(self):
        if not hasattr(self, '_model'):
            self._model = self.get_content_type().model_class()
        return self._model

    def get_template_names(self, *args, **kwargs):
        return ['admin/{0}/{1}/_list.html'.format(
                self.get_model()._meta.app_label,
                self.get_model()._meta.object_name.lower())]

    def get_queryset(self):
        pk_list = filter(bool, self.request.REQUEST.get('pks', '').split(','))
        objects = self.get_model().objects.active().in_bulk(pk_list)
        return (objects.get(int(pk)) for pk in pk_list)

    def post(self, *args, **kwargs):
        return self.get(*args, **kwargs)
