from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from mimetypes import guess_type
from thecut.managers import QuerySetManager
from thecut.models import AbstractSitesResourceWithSlug


class MediaSet(models.Model):
    """A collection of media (photos/galleries/documents)."""
    # Generic relation to an object.
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField()
    content_object = generic.GenericForeignKey('content_type',
        'object_id')
    
    images = models.ManyToManyField('photologue.Photo',
        null=True, blank=True)
    image_order = models.CommaSeparatedIntegerField(max_length=250,
        null=True, blank=True)
    galleries = models.ManyToManyField('media.Gallery',
        null=True, blank=True)
    documents = models.ManyToManyField('Document', null=True,
        blank=True)
    
    class Meta:
        unique_together = ['content_type', 'object_id']
    
    @property
    def ordered_images(self):
        """Return an ordered list of images.
        
        Ordered list is defined by the model's image_order field.
        
        """
        images = list(self.images.all())

        if self.image_order:
            image_order = [int(pk) for pk in self.image_order.split(',')]
            try:
                images = sorted(images, key=lambda image: image_order.index(image.pk))
            except ValueError:
                # image ordering has been corrupted
                pass
        return images
    
    @property
    def all_images(self):
        """Return all images and all gallery images."""
        images = self.ordered_images
        for gallery in self.galleries.all():
            images += list(gallery.images.all())
        return images
    
    @property
    def image(self):
        """Return the first image from all_images, if one exists."""
        try:
            image = self.all_images[0]
        except IndexError:
            image = None
        return image
    
    @property
    def photo(self):
        """Deprecated - instead use 'image'."""
        return self.image
    
    @property
    def photos(self):
        """Deprecated - instead use 'images'."""
        return self.images
    
    @property
    def all_photos(self):
        """Deprecated - instead use 'all_images'."""
        return self.all_images


class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='uploads/documents')
    
    created_at = models.DateTimeField(auto_now_add=True,
        editable=False)
    created_by = models.ForeignKey(User, editable=False,
        related_name='document_created_by_user')
    
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    updated_by = models.ForeignKey(User, editable=False,
        related_name='document_updated_by_user')
    
    class Meta:
        get_latest_by = 'created_at'
        ordering = ['title']
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return self.file.url
    
    @property
    def mime_type(self):
        """Guess the MIME type of this document."""
        return guess_type(self.file.path)[0]


class Gallery(AbstractSitesResourceWithSlug):
    """Image gallery."""
    images = models.ManyToManyField('photologue.Photo',
        null=True, blank=True)
    #TODO: Image ordering
    
    objects = QuerySetManager()
    
    class Meta(AbstractSitesResourceWithSlug.Meta):
        ordering = ['-publish_at', 'title']
        verbose_name_plural = 'galleries'
    
    def get_absolute_url(self):
        return reverse('gallery_detail', kwargs={'slug': self.slug})
    
    @property
    def image(self):
        """Return the first image from all_images, if one exists."""
        try:
            #image = self.all_images[0]
            image = self.images.all()[0]
        except IndexError:
            image = None
        return image
    
    @property
    def photos(self):
        """Deprecated - instead use 'images'."""
        return self.images

