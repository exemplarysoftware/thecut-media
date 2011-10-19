# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic.list_detail import object_list
from django.views.decorators.cache import cache_control, cache_page
from tagging.models import Tag, TaggedItem
from thecut.media import MEDIA_SOURCE_CLASSES
from thecut.media.forms import MediaSearchForm


PAGINATE_BY = getattr(settings, 'MEDIA_PAGINATE_BY', 7)


@cache_control(no_cache=True)
@cache_page(0)
@user_passes_test(lambda u: u.has_perm('media.add_attachedmediaitem') or \
    u.has_perm('media.change_attachedmediaitem'))
def admin_contenttype_list(request):
    if request.is_ajax() or settings.DEBUG:
        content_types = [ContentType.objects.get_for_model(model) for \
            model in MEDIA_SOURCE_CLASSES]
        return render_to_response('media/_contenttype_list.html',
            {'content_type_list': content_types})
    else:
        return HttpResponseBadRequest('bad request')


@cache_control(no_cache=True)
@cache_page(0)
@user_passes_test(lambda u: u.has_perm('media.add_attachedmediaitem') or \
    u.has_perm('media.change_attachedmediaitem'))
def admin_contenttype_object_list(request, content_type_pk,
    queryset=None, **kwargs):
    if request.is_ajax() or settings.DEBUG:
        content_type = get_object_or_404(ContentType,
            pk=content_type_pk)
        model_class = content_type.model_class()
        object_name = model_class._meta.object_name.lower()
        template_name = 'admin/%s/%s/_picker.html' %(
            content_type.app_label, object_name)
        
        if queryset is None:
            queryset = model_class.objects.active()
        tag_list = Tag.objects.usage_for_queryset(queryset,
            counts=True)
        
        form = MediaSearchForm(tag_list, request.GET)
        valid = form.is_valid()
        
        q = form.cleaned_data.get('q', None)
        if q:
            queryset = queryset.filter(title__icontains=q)
        
        selected_tag_pks = form.cleaned_data.get('tags', None)
        if selected_tag_pks:
            queryset = TaggedItem.objects.get_intersection_by_model(
                queryset, Tag.objects.filter(pk__in=selected_tag_pks))
            tag_list = Tag.objects.usage_for_queryset(queryset,
                counts=True)
        
        form = MediaSearchForm(tag_list, initial={'q': q,
            'tags': selected_tag_pks})
        
        extra_context = {'content_type': content_type, 'form': form}
        kwargs.update({'extra_context': extra_context})
        
        kwdefaults = {'paginate_by': PAGINATE_BY,
            'template_name': template_name,
            'template_object_name': object_name}
        kwdefaults.update(kwargs)
        
        return object_list(request, queryset, **kwdefaults)
    else:
        return HttpResponseBadRequest('Bad request.')


@cache_control(no_cache=True)
@cache_page(0)
@user_passes_test(lambda u: u.has_perm('media.add_attachedmediaitem') or \
    u.has_perm('media.change_attachedmediaitem'))
def admin_contenttype_selected_object_list(request, content_type_pk):
    if request.is_ajax() or settings.DEBUG:
        content_type = get_object_or_404(ContentType,
            pk=content_type_pk)
        model_class = content_type.model_class()
        object_name = model_class._meta.object_name.lower()
        template_name = 'admin/%s/%s/_list.html' %(
            content_type.app_label, object_name)
        
        pks = request.REQUEST.get('pks', None)
        pks = pks and pks.split(',') or []
        object_dictionary = pks and model_class.objects.active().in_bulk(
            pks) or {}
        
        objects = [object_dictionary.get(int(pk)) for pk in pks]
        
        return render_to_response(template_name,
            {'%s_list' %(object_name): objects, 'content_type': content_type})
    else:
        return HttpResponseBadRequest('Bad request.')

