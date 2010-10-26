from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from media.models import Gallery, Video


class GallerySitemap(Sitemap):
    """Sitemaps.org XML sitemap."""
    def items(self):
        return Gallery.objects.current_site().indexable()
    
    def lastmod(self, obj):
        return obj.updated_at


class VideoSitemap(Sitemap):
    """Sitemaps.org XML sitemap."""
    def items(self):
        return Video.objects.current_site().indexable()
    
    def lastmod(self, obj):
        return obj.updated_at


class View(object):
    """Wrapper for a view in order to provide get_absolute_url()."""
    def __init__(self, name):
        self.name = name
    
    def get_absolute_url(self):
        return reverse(self.name)


class MediaSitemap(Sitemap):
    def items(self):
        return [View('gallery_list'), View('video_list')]


sitemaps = {'media': MediaSitemap, 'galleries': GallerySitemap,
    'videos': VideoSitemap}

