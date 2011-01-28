from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from mimetypes import guess_type
from photologue.models import Photo
from thecut.managers import QuerySetManager
from thecut.media.utils import generate_unique_image_slug
from thecut.media.signals import set_publish_at
from thecut.models import AbstractBaseResource, AbstractSitesResourceWithSlug
import warnings


class MediaSet(models.Model):
    """A collection of media (images/galleries/documents)."""
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
            images += gallery.all_images
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
        warnings.warn("Deprecated - use 'image' property.",
            DeprecationWarning)
        return self.image
    
    @property
    def photos(self):
        """Deprecated - instead use 'images'."""
        warnings.warn("Deprecated - use 'images' property.",
            DeprecationWarning)
        return self.images
    
    @property
    def all_photos(self):
        """Deprecated - instead use 'all_images'."""
        warnings.warn("Deprecated - use 'all_images' property.",
            DeprecationWarning)
        return self.all_images


class Image(Photo):
    class Meta(Photo.Meta):
        proxy = True
    
    def save(self, *args, **kwargs):
        if not self.title_slug:
            self.title_slug = generate_unique_image_slug(self.title)
        super(Image, self).save(*args, **kwargs)


class Document(AbstractBaseResource):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='uploads/documents')
    
    objects = QuerySetManager()
    
    class Meta(AbstractBaseResource.Meta):
        ordering = ['-publish_at', 'title']
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return self.file.url
    
    @property
    def mime_type(self):
        """Guess the MIME type of this document."""
        return guess_type(self.file.path)[0]

models.signals.post_init.connect(set_publish_at, sender=Document)


class Gallery(AbstractSitesResourceWithSlug):
    """Image gallery."""
    images = models.ManyToManyField('photologue.Photo',
        null=True, blank=True)
    image_order = models.CommaSeparatedIntegerField(max_length=250,
        null=True, blank=True)
    
    objects = QuerySetManager()
    
    class Meta(AbstractSitesResourceWithSlug.Meta):
        ordering = ['-publish_at', 'title']
        verbose_name_plural = 'galleries'
    
    class QuerySet(AbstractSitesResourceWithSlug.QuerySet):
        def with_images(self):
            """Return active objects containg at least one image."""
            return self.annotate(
                num_images=models.Count('images')).filter(
                num_images__gte=1)
    
    @models.permalink
    def get_absolute_url(self):
        return ('gallery_detail', [], {'slug': self.slug})
    
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
        """Return all images."""
        return self.ordered_images
    
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
        warnings.warn("Deprecated - use 'image' property.",
            DeprecationWarning)
        return self.image
    
    @property
    def photos(self):
        """Deprecated - instead use 'images'."""
        warnings.warn("Deprecated - use 'images' property.",
            DeprecationWarning)
        return self.images
    
    @property
    def all_photos(self):
        """Deprecated - instead use 'all_images'."""
        warnings.warn("Deprecated - use 'all_images' property.",
            DeprecationWarning)
        return self.all_images


class Video(AbstractSitesResourceWithSlug):
    file = models.FileField(upload_to='uploads/videos')
    thumbnail = models.ImageField(upload_to='uploads/videos/thumbnails',
        null=True, blank=True)
    
    objects = QuerySetManager()
    
    class Meta(AbstractSitesResourceWithSlug.Meta):
        ordering = ['-publish_at', 'title']
    
    @models.permalink
    def get_absolute_url(self):
        return ('video_detail', [], {'slug': self.slug})
    
    def generate_thumbnail(self):
        if self.thumbnail:
            self.thumbnail.delete()
        import subprocess
        from django.conf import settings
        from django.core.files.images import ImageFile
        from django.template.defaultfilters import slugify
        file_name = slugify(self.title)
        file_path = '%s/%s.jpg' %('uploads/videos/thumbnails', file_name)
        command_line = 'ffmpegthumbnailer -i %s -o %s/%s -s %d' % (self.file.path, settings.MEDIA_ROOT, file_path, 720)
        subprocess.check_call(command_line, shell=True)#, stderr=subprocess.STDOUT)
        thumbnail = file_path#ImageFile(open(file_path, 'rb'))
        self.thumbnail = thumbnail
        self.save()
    
    @property
    def image(self):
        return self.thumbnail
    
    @property
    def mime_type(self):
        """Guess the MIME type of this video."""
        return guess_type(self.file.path)[0]
    
    def save(self, *args, **kwargs):
        response = super(Video, self).save(*args, **kwargs)
        if not self.thumbnail:
            self.generate_thumbnail()
        return response

