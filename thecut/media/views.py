from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.list_detail import object_detail, object_list
from thecut.media.forms import DocumentUploadForm, ImageUploadForm
from thecut.media.models import Gallery, Video


PAGINATE_BY = getattr(settings, 'MEDIA_PAGINATE_BY', 100)
NO_IMAGE_404 = getattr(settings, 'MEDIA_NO_IMAGE_404', True)


def gallery_list(request, page=None):
    if page == '1':
        return redirect(reverse('gallery_list'))
    if page is None:
        page = 1
    queryset = Gallery.objects.current_site().active()
    
    return object_list(request, queryset, paginate_by=PAGINATE_BY,
        page=page, template_object_name='gallery')


def gallery_detail(request, slug):
    if NO_IMAGE_404:
        queryset = Gallery.objects.current_site().active().with_images()
    else:
        queryset = Gallery.objects.current_site().active()
    if 'facebook' in settings.INSTALLED_APPS:
        template_name = 'media/gallery_detail_facebook.html'
    else:
        template_name = None
    return object_detail(request, queryset, slug=slug,
        template_name=template_name, template_name_field='template',
        template_object_name='gallery')


def video_list(request, page=None):
    if page == '1':
        return redirect(reverse('video_list'))
    if page is None:
        page = 1
    queryset = Video.objects.current_site().active()
    
    return object_list(request, queryset, paginate_by=PAGINATE_BY,
        page=page, template_object_name='video')


def video_detail(request, slug):
    queryset = Video.objects.current_site().active()
    if 'facebook' in settings.INSTALLED_APPS:
        template_name = 'media/video_detail_facebook.html'
    else:
        template_name = None
    return object_detail(request, queryset, slug=slug,
        template_name=template_name, template_name_field='template',
        template_object_name='video')


def document_picker(request):
    """Document picker."""
    if not request.is_ajax():
        return HttpResponseBadRequest('error')
    
    #TODO: Get the queryset specified passed to
    # DocumentMultipleChoiceField? Form post/session?
    from thecut.media.models import Document
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


@permission_required('media.add_document')
def document_upload(request):
    """Document upload."""
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            return render_to_response(
                'media/_document_upload_complete.html',
                {'document': document},
                context_instance=RequestContext(request))
    else:
        form = DocumentUploadForm()
    return render_to_response('media/_document_upload.html',
        {'form': form},
        context_instance=RequestContext(request))


def gallery_picker(request):
    """Gallery picker."""
    if not request.is_ajax():
        return HttpResponseBadRequest('error')
    
    #TODO: Get the queryset specified passed to
    # GalleryMultipleChoiceField? Form post/session?
    from thecut.media.models import Gallery
    queryset = Gallery.objects.active()
    
    paginate_by = PAGINATE_BY
    
    ids = request.REQUEST.get('ids', None)
    if ids:
       ids = ids.split(',')
       queryset = queryset.filter(pk__in=ids)
       # Disable Pagination
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
    from thecut.media.models import Image
    queryset = Image.objects.filter(is_public=True)
    
    paginate_by = PAGINATE_BY
    
    q = request.REQUEST.get('q', None)
    if q:
        queryset = queryset.filter(title__icontains=q)
    
    ids = request.REQUEST.get('ids', None)
    if ids:
       ids = ids.split(',')
       queryset = queryset.filter(pk__in=ids)
       paginate_by = queryset.count()
       querylist = []
       for pk in ids:
           querylist += [queryset.get(pk=pk)]
       queryset = querylist
    
    return render_to_response('media/_image_picker.html',
        {'photo_list': queryset, 'q': q},
        context_instance=RequestContext(request))


@permission_required('photologue.add_photo')
def image_upload(request):
    """Image upload."""
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            return render_to_response(
                'media/_image_upload_complete.html', {'image': image},
                context_instance=RequestContext(request))
    else:
        form = ImageUploadForm()
    return render_to_response('media/_image_upload.html',
        {'form': form},
        context_instance=RequestContext(request))


if getattr(settings, 'DEBUG', False):
    def image_picker_test(request):
        from django.forms import Form, ModelMultipleChoiceField
        from django.shortcuts import render_to_response
        from django.template import RequestContext
        from thecut.media.fields import ImageMultipleChoiceField
        from thecut.media.models import Image
        
        class TestForm(Form):
            photos1 = ImageMultipleChoiceField(Image.objects.all())
            photos2 = ImageMultipleChoiceField(Image.objects.all())
        
        form = TestForm()
        
        return render_to_response('media/image_picker_test.html',
            {'form': form}, context_instance=RequestContext(request))


