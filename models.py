from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from mimetypes import guess_type


class MediaSet(models.Model):
    """A collection of media (photos/galleries/documents)."""
    # Generic relation to an object.
    content_type = models.ForeignKey(ContentType)
    object_id = models.TextField()
    content_object = generic.GenericForeignKey('content_type',
        'object_id')
    
    photos = models.ManyToManyField('photologue.Photo',
        through='AttachedPhoto', null=True, blank=True)
    galleries = models.ManyToManyField('photologue.Gallery',
        null=True, blank=True)
    documents = models.ManyToManyField('Document', null=True,
        blank=True)
    
    class Meta:
        unique_together = ['content_type', 'object_id']
    
    @property
    def photo(self):
        """Return the first photo from all_photos, if one exists."""
        try:
            photo = self.all_photos[0]
        except IndexError:
            photo = None
        return photo
    
    @property
    def all_photos(self):
        """Return all photos and all gallery photos."""
        photos = list(self.photos.order_by('attachedphoto__order'))
        for gallery in self.galleries.all():
            photos += list(gallery.photos.all())
        return photos


class AttachedPhoto(models.Model):
    photo = models.ForeignKey('photologue.Photo')
    mediaset = models.ForeignKey('MediaSet')
    order = models.PositiveSmallIntegerField(default=0)
    
    class Meta:
        ordering = ['order', '-photo__date_added']
    
    def __unicode__(self):
        return self.photo.__unicode__()
    
    def get_absolute_url(self):
        return self.photo.get_absolute_url()


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

