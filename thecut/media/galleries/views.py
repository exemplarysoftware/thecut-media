# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from thecut.media.galleries import settings
from thecut.media.galleries.models import Gallery, GalleryCategory


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
            category = self.get_category()
            if category:
                return redirect('galleries:category_gallery_list',
                                slug=category.slug, permanent=True)
            else:
                return redirect('galleries:gallery_list', permanent=True)
        return super(ListView, self).get(*args, **kwargs)

    def get_category(self):
        if not hasattr(self, '_category'):
            slug = self.kwargs.get('slug', None)
            if slug is not None:
                category = get_object_or_404(GalleryCategory.objects.active(),
                                             slug=slug)
            else:
                category = None
            self._category = category
        return self._category

    def get_context_data(self, *args, **kwargs):
        context_data = super(ListView, self).get_context_data(*args, **kwargs)
        category = self.get_category()
        context_data.setdefault('category', category)
        return context_data

    def get_queryset(self, *args, **kwargs):
        queryset = super(ListView, self).get_queryset(*args, **kwargs)
        category = self.get_category()
        if category:
            queryset = queryset.filter(categories=category)
        return queryset.current_site().active()


class MediaListView(generic.ListView):

    context_object_name = 'gallery_media_list'
    paginate_by = settings.GALLERY_MEDIA_PAGINATE_BY
    template_name = 'galleries/gallery_media_list.html'
    template_name_field = 'template'
    _gallery = None

    def get_template_names(self, *args, **kwargs):
        """Select the template to render.

        Basic reimplementation of SingleObjectTemplateResponseMixin's
        get_template_name(). Renders with the gallery object's template
        property if it's set.
        """
        templates = super(MediaListView, self).get_template_names(
            *args, **kwargs)
        gallery = self.get_gallery()
        if gallery:
            model_template = getattr(gallery, self.template_name_field, None)
            if model_template:
                templates = [model_template] + templates
        return templates

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
