from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.utils.feedgenerator import Atom1Feed
from thecut.media.galleries.models import Gallery


class LatestGalleryFeed(Feed):
    feed_type = Atom1Feed
    subtitle = 'Latest galleries.'
    
    def link(self):
        return reverse('galleries:gallery_list')
    
    def title(self):
        site = Site.objects.get_current()
        return '%s - Galleries' %(site.name)
    
    def items(self):
        return Gallery.objects.current_site().active().order_by(
            '-publish_at')[:10]
    
    def item_title(self, item):
        return str(item)
    
    def item_description(self, item):
        return item.content
    
    def item_pubdate(self, item):
        return item.publish_at

