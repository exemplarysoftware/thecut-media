# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, redirect
from thecut.media.galleries import settings
from thecut.media.galleries.models import Gallery

# Class-based views
from distutils.version import StrictVersion
from django import get_version
if StrictVersion(get_version()) < StrictVersion('1.3'):
    import cbv as generic
else:
    from django.views import generic


class DetailView(generic.DetailView):
    context_object_name = 'gallery'
    model = Gallery
    template_name_field = 'template'
    
    def get_queryset(self, *args, **kwargs):
        queryset = super(DetailView, self).get_queryset(*args, **kwargs)
        return queryset.current_site().active()


class ListView(generic.ListView):
    context_object_name = 'gallery_list'
    model = Gallery
    paginate_by = settings.GALLERY_PAGINATE_BY
    
    def get(self, *args, **kwargs):
        page = self.kwargs.get('page', None)
        if page is not None and int(page) < 2:
            return redirect('galleries:gallery_list', permanent=True)
        return super(ListView, self).get(*args, **kwargs)
    
    def get_queryset(self, *args, **kwargs):
        queryset = super(ListView, self).get_queryset(*args, **kwargs)
        return queryset.current_site().active()


class MediaListView(generic.ListView):
    context_object_name = 'gallery_media_list'
    paginate_by = settings.GALLERY_MEDIA_PAGINATE_BY
    template_name = 'galleries/gallery_media_list.html'
    _gallery = None
    
    def get(self, *args, **kwargs):
        page = self.kwargs.get('page', None)
        if page is not None and int(page) < 2:
            return redirect('galleries:gallery_media_list',
                slug=self.get_gallery().slug, permanent=True)
        return super(MediaListView, self).get(*args, **kwargs)
    
    def get_context_data(self, *args, **kwargs):
        context_data = super(MediaListView, self).get_context_data(*args,
            **kwargs)
        context_data.update({'gallery': self.get_gallery()})
        return context_data
    
    def get_gallery(self):
        if self._gallery is None:
            self._gallery = get_object_or_404(
                Gallery.objects.current_site().active(),
                slug=self.kwargs.get('slug', None))
        return self._gallery
    
    def get_queryset(self, *args, **kwargs):
        return self.get_gallery().media.all()

