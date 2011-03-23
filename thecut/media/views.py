from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.utils import simplejson
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
            queryset = queryset.filter(title__contains=q)
        
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
        
        #if kwargs.get('page', None) == '1':
        #    return redirect('../')
        kwdefaults = {'paginate_by': PAGINATE_BY, #'page': 1,
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
def admin_contenttype_object_detail(request, content_type_pk,
    object_pk):
    if request.is_ajax() or settings.DEBUG:
        content_type = get_object_or_404(ContentType,
            pk=content_type_pk)
        model_class = content_type.model_class()
        object_name = model_class._meta.object_name.lower()
        obj = get_object_or_404(model_class.objects.active(),
            pk=object_pk)
        template = 'admin/%s/%s/_list_item.html' %(
            content_type.app_label, object_name)
        return render_to_response(template, {object_name: obj,
            'content_type': content_type})
    else:
        return HttpResponseBadRequest('bad request')

