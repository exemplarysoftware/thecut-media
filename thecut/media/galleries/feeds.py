# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.utils.feedgenerator import Atom1Feed
from thecut.media.galleries.models import Gallery, GalleryCategory


class LatestGalleryFeed(Feed):

    feed_type = Atom1Feed
    subtitle = 'Latest galleries.'

    def link(self):
        return reverse('galleries:gallery_list')

    def title(self):
        site = Site.objects.get_current()
        return '{0} - Galleries'.format(site.name)

    def items(self):
        return Gallery.objects.current_site().active().order_by(
            '-publish_at')[:10]

    def item_title(self, item):
        return '{0}'.format(item)

    def item_description(self, item):
        return item.content

    def item_pubdate(self, item):
        return item.publish_at


class LatestCategoryGalleryFeed(Feed):

    feed_type = Atom1Feed

    def title(self, obj):
        return 'Latest {0}'.format(obj)

    def link(self, obj):
        return reverse('galleries:category_gallery_list',
                       kwargs={'slug': obj.slug})

    def get_object(self, request, slug):
        return get_object_or_404(GalleryCategory, slug=slug)

    def items(self, obj):
        return obj.galleries.current_site().active().order_by(
            '-publish_at')[:10]

    def item_title(self, item):
        return str(item)

    def item_description(self, item):
        return item.content

    def item_pubdate(self, item):
        return item.publish_at
