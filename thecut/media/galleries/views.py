# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list_detail import object_detail, object_list
from thecut.media.galleries import settings
from thecut.media.galleries.models import Gallery


def gallery_list(request, queryset=None, **kwargs):
    if queryset is None:
        queryset = Gallery.objects.current_site().active()
    
    if kwargs.get('page', None) == '1':
        return redirect(reverse('galleries:gallery_list'))
    kwdefaults = {'paginate_by': settings.GALLERY_PAGINATE_BY, 'page': 1,
        'template_object_name': 'gallery'}
    kwdefaults.update(kwargs)
    
    return object_list(request, queryset, **kwdefaults)


def gallery_detail(request, queryset=None, **kwargs):
    if queryset is None:
        queryset = Gallery.objects.current_site().active()
    
    kwdefaults = {'template_name_field': 'template',
        'template_object_name': 'gallery'}
    kwdefaults.update(kwargs)
    
    return object_detail(request, queryset, **kwdefaults)


def gallery_media_list(request, slug, queryset=None, **kwargs):
    gallery = get_object_or_404(Gallery.objects.current_site().active(),
        slug=slug)
    
    if queryset is None:
        queryset = gallery.media.all()
    
    if kwargs.get('page', None) == '1':
        return redirect(reverse('galleries:gallery_media_list',
            kwargs={'slug': gallery.slug}))
    
    kwargs.update({'extra_context': {'gallery': gallery}})
    kwdefaults = {'paginate_by': settings.GALLERY_MEDIA_PAGINATE_BY, 'page': 1,
        'template_name': 'galleries/gallery_media_list.html',
        'template_object_name': 'gallery_media'}
    kwdefaults.update(kwargs)
    
    return object_list(request, queryset, **kwdefaults)

