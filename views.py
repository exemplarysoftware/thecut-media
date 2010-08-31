from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic.list_detail import object_list


PAGINATE_BY = getattr(settings, 'MEDIA_PAGINATE_BY', 100)


def document_picker(request):
    """Document picker."""
    if not request.is_ajax():
        return HttpResponseBadRequest('error')
    
    #TODO: Get the queryset specified passed to
    # GalleryMultipleChoiceField? Form post/session?
    from media.models import Document
    queryset = Document.objects.all()#filter(is_public=True)
    
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
        template_name='media/_document_picker.html',
        template_object_name='document')


def gallery_picker(request):
    """Gallery picker."""
    if not request.is_ajax():
        return HttpResponseBadRequest('error')
    
    #TODO: Get the queryset specified passed to
    # GalleryMultipleChoiceField? Form post/session?
    from photologue.models import Gallery
    queryset = Gallery.objects.filter(is_public=True)
    
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
        template_name='media/_gallery_picker.html',
        template_object_name='gallery')


def image_picker(request):
    """Image picker."""
    if not request.is_ajax():
        return HttpResponseBadRequest('error')
    
    #TODO: Get the queryset specified passed to
    # ImageMultipleChoiceField? Form post/session?
    from photologue.models import Photo
    queryset = Photo.objects.filter(is_public=True)
    
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


if getattr(settings, 'DEBUG', False):
    def image_picker_test(request):
        from django.forms import Form, ModelMultipleChoiceField
        from django.shortcuts import render_to_response
        from django.template import RequestContext
        from media.fields import ImageMultipleChoiceField
        from photologue.models import Photo
        
        class TestForm(Form):
            photos1 = ImageMultipleChoiceField(Photo.objects.all())
            photos2 = ImageMultipleChoiceField(Photo.objects.all())
        
        form = TestForm()
        
        return render_to_response('media/image_picker_test.html',
            {'form': form}, context_instance=RequestContext(request))


