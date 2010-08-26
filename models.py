from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models

try:
    from magic import Magic
except ImportError:
    Magic = None


class MediaSet(models.Model):
    """A collection of media (photos/galleries/documents)."""
    # Generic relation to an object.
    content_type = models.ForeignKey(ContentType)
    object_id = models.TextField()
    content_object = generic.GenericForeignKey('content_type',
        'object_id')
    
    photos = models.ManyToManyField('photologue.Photo', null=True,
        blank=True)
    galleries = models.ManyToManyField('photologue.Gallery',
        null=True, blank=True)
    documents = models.ManyToManyField('Document', null=True,
        blank=True)
    
    class Meta:
        unique_together = ['content_type', 'object_id']
    
    @property
    def photo(self):
        """Return the first photo from photos.all(), if one exists."""
        try:
            photo = self.photos.all()[0]
        except IndexError:
            photo = None
        return photo


class Document(models.Model):
    name = models.CharField(max_length=200)
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
        ordering = ['name']
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return self.file.url
    
    @property
    def mime_type(self):
        """Determine the MIME type of this document.
        
        Requires recent version of python-magic from
        http://github.com/ahupp/python-magic
        
        """
        if Magic:
            magic = Magic(mime=True)
            mime = magic.from_file(self.file.path)
        else:
            mime = None
        return mime

