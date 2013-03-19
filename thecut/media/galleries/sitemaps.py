# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.sitemaps import Sitemap
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from thecut.media.galleries import settings
from thecut.media.galleries.models import Gallery, GalleryCategory


class GallerySitemap(Sitemap):
    """Sitemaps.org XML sitemap."""

    def items(self):
        return Gallery.objects.current_site().indexable()

    def lastmod(self, obj):
        return obj.updated_at


class GalleryListSitemap(Sitemap):

    def items(self):
        objects = Gallery.objects.current_site().indexable()
        page_size = settings.GALLERY_PAGINATE_BY
        return Paginator(objects, page_size).page_range if page_size else [1]

    def location(self, page):
        if page == 1:
            return reverse('galleries:gallery_list')
        else:
            return reverse('galleries:paginated_gallery_list',
                           kwargs={'page': page})


class CategoryGalleryListSitemap(Sitemap):

    def items(self):
        categories = GalleryCategory.objects.indexable()
        items = []
        for category in categories:
            objects = category.galleries.current_site().indexable()
            page_size = settings.GALLERY_PAGINATE_BY
            page_range = Paginator(objects, page_size).page_range if \
                page_size else [1]
            items += [(category.slug, page) for page in page_range]
        return items

    def location(self, opts):
        slug, page = opts
        if page == 1:
            return reverse('galleries:category_gallery_list',
                           kwargs={'slug': slug})
        else:
            return reverse('galleries:paginated_category_gallery_list',
                           kwargs={'slug': slug, 'page': page})


sitemaps = {'galleries_gallery': GallerySitemap,
            'galleries_gallerylist': GalleryListSitemap,
            'galleries_categorygallerylist': CategoryGalleryListSitemap}
