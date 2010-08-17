from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic.list_detail import object_list


PAGINATE_BY = getattr(settings, 'MEDIA_PAGINATE_BY', 3)

if getattr(settings, 'DEBUG', False):
    def test(request):
        from django.forms import Form, ModelMultipleChoiceField
        from django.shortcuts import render_to_response
        from django.template import RequestContext
        from media.fields import ImageMultipleChoiceField
        from photologue.models import Photo
        
        class TestForm(Form):
            photos1 = ImageMultipleChoiceField(Photo.objects.all())
            photos2 = ImageMultipleChoiceField(Photo.objects.all())
        
        form = TestForm()
        
        return render_to_response('media/test.html', {'form': form},
            context_instance=RequestContext(request))


def image_picker(request):
    """Image picker."""
    #if not request.is_ajax():
    #    return HttpResponseBadRequest('error')
    
    #TODO: Get the queryset specified passed to
    # ImageMultipleChoiceField? Form post/session?
    from photologue.models import Photo
    queryset = Photo.objects.filter()
    
    paginate_by = PAGINATE_BY
    
    ids = request.REQUEST.get('ids', None)
    if ids:
       ids = ids.split(',')
       queryset = queryset.filter(pk__in=ids)
       paginate_by = queryset.count()
    
    q = request.REQUEST.get('q', None)
    if q:
        queryset = queryset.filter(title__icontains=q)
    
    return object_list(request, queryset, extra_context={'q': q},
        paginate_by=paginate_by,
        template_name='media/_image_picker.html',
        template_object_name='photo')

