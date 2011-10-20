# -*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from thecut.media.galleries import settings
from thecut.media.galleries.models import Gallery


class GallerySitemap(Sitemap):
    """Sitemaps.org XML sitemap."""
    def items(self):
        return Gallery.objects.current_site().indexable()
    
    def lastmod(self, obj):
        return obj.updated_at


class GalleryListSitemap(Sitemap):
    def items(self):
        objects = Gallery.objects.current_site().indexable()
        paginator = Paginator(objects, settings.GALLERY_PAGINATE_BY)
        return paginator.page_range
    
    def location(self, page):
        if page == 1:
            return reverse('galleries:gallery_list')
        else:
            return reverse('galleries:paginated_gallery_list',
                kwargs={'page': page})


sitemaps = {'galleries_gallery': GallerySitemap,
    'galleries_gallerylist': GalleriesSitemap}

