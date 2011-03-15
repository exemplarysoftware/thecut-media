from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.utils import simplejson
from django.views.decorators.cache import cache_control, cache_page
from thecut.media import MEDIA_SOURCE_CLASSES


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
@user_passes_test(lambda u: u.has_perm('ctas.add_calltoaction') or \
    u.has_perm('ctas.change_calltoaction'))
def admin_contenttype_object_list(request, content_type_pk):
    #"""Add/create new child menu."""
    if request.is_ajax() or settings.DEBUG:
        content_type = get_object_or_404(ContentType,
            pk=content_type_pk)
        model_class = content_type.model_class()
        
        objects = []
        for obj in model_class.objects.all():
            name = str(obj)
            if hasattr(obj, 'sites'):
                try:
                    name += ' (%s)' %(', '.join(
                        [site.name for site in obj.sites.all()]))
                except:
                    pass
            if hasattr(obj, 'site'):
                try:
                    name += ' (%s)' %(obj.site.name)
                except:
                    pass
            objects += [{'pk': obj.pk, 'name': name}]
        
        return HttpResponse(simplejson.dumps(objects),
            mimetype='application/json')
    else:
        return HttpResponseBadRequest('bad request')


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

