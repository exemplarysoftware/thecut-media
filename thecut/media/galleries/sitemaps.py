from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from thecut.media.galleries.models import Gallery


class GallerySitemap(Sitemap):
    """Sitemaps.org XML sitemap."""
    def items(self):
        return Gallery.objects.current_site().indexable()
    
    def lastmod(self, obj):
        return obj.updated_at


class View(object):
    """Wrapper for a view in order to provide get_absolute_url()."""
    def __init__(self, name):
        self.name = name
    
    def get_absolute_url(self):
        return reverse(self.name)


class GalleriesSitemap(Sitemap):
    def items(self):
        return [View('galleries:gallery_list')]


sitemaps = {'gallery': GallerySitemap, 'galleries': GalleriesSitemap}

