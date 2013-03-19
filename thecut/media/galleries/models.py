# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from thecut.publishing.models import Content, SiteContentWithSlug
from thecut.publishing.utils import generate_unique_slug


class AbstractGallery(SiteContentWithSlug):

    class Meta(SiteContentWithSlug.Meta):
        abstract = True
        ordering = ('-publish_at', 'title')
        verbose_name_plural = 'galleries'


class AbstractGalleryCategory(Content):

    slug = models.SlugField(unique=True)

    class Meta(Content.Meta):
        abstract = True
        verbose_name_plural = 'gallery categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(
                self.title, self.__class__.objects.all())
        return super(AbstractGalleryCategory, self).save(*args, **kwargs)


class Gallery(AbstractGallery):

    categories = models.ManyToManyField('galleries.GalleryCategory',
                                        related_name='galleries', blank=True,
                                        null=True)

    def get_absolute_url(self):
        return reverse('galleries:gallery_media_list',
                       kwargs={'slug': self.slug})


class GalleryCategory(AbstractGalleryCategory):

    def get_absolute_url(self):
        return reverse('galleries:category_gallery_list',
                       kwargs={'slug': self.slug})
