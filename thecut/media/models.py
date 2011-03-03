from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from functools import partial
from tagging.fields import TagField
from thecut.core.managers import QuerySetManager
from thecut.core.models import AbstractBaseResource
import warnings


class AbstractMediaItem(AbstractBaseResource):
    title = models.CharField(max_length=200)
    caption = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    tags = TagField(null=True, blank=True, help_text='Separate tags \
        with spaces, put quotes around multiple-word tags.')
    
    objects = QuerySetManager()
    
    class Meta(AbstractBaseResource.Meta):
        abstract = True
    
    def __unicode__(self):
        return self.title


class MediaSet(models.Model):
    # Generic relation to an object.
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField()
    content_object = generic.GenericForeignKey('content_type',
        'object_id')
    
    class Meta:
        unique_together = ['content_type', 'object_id']
    
    def get_image(self):
        #return self.items.all()[0].get_image()
        return self.items.images()[0].get_image()
    
    ## Deprecated properties
    
    @property
    def all_images(self):
        """Deprecated - instead use 'items.images()'."""
        warnings.warn('all_images property is deprecated - use '
            '\'items.images()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.items.images()
    
    @property
    def all_photos(self):
        """Deprecated - instead use 'items.images()'."""
        warnings.warn('all_photos property is deprecated - use '
            '\'items.images()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.items.images()
    
    @property
    def documents(self):
        """Deprecated - instead use 'items.documents()'."""
        warnings.warn('documents property is deprecated - use '
            '\'items.documents()\' method.', DeprecationWarning,
            stacklevel=2)
        documents = self.items.documents
        class proxy(object):
            def all(self):
                return documents()
        return proxy()
    
    @property
    def galleries(self):
        """Deprecated. Galleries cannot be attached to MediaSets."""
        warnings.warn('Galleries can no longer be attached to '
            'MediaSets.', DeprecationWarning, stacklevel=2)
        class proxy(object):
            def all(self):
                return None
        return proxy()
    
    @property
    def image(self):
        """Deprecated - instead use 'get_image()'."""
        warnings.warn('image property is deprecated - use '
            '\'get_image()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.get_image()
    
    @property
    def image_order(self):
        """Deprecated. Ordering is now managed by AttachedMediaItem."""
        warnings.warn('Ordering is now managed by AttachedMediaItem '
            'model.', DeprecationWarning, stacklevel=2)
        return [image.pk for image in self.items.images()]
    
    @property
    def images(self):
        """Deprecated - instead use 'items.images()'."""
        warnings.warn('images property is deprecated - use '
            '\'items.images()\' method.', DeprecationWarning,
            stacklevel=2)
        images = self.items.images
        class proxy(object):
            def all(self):
                return images()
        return proxy()
    
    @property
    def ordered_images(self):
        """Deprecated - instead use 'items.images()'."""
        warnings.warn('ordered_images property is deprecated - use '
            '\'items.images()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.items.images()
    
    @property
    def photo(self):
        """Deprecated - instead use 'get_image()'."""
        warnings.warn('photo property is deprecated - use '
            '\'get_image()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.get_image()
    
    @property
    def photos(self):
        """Deprecated - instead use 'items.images()'."""
        warnings.warn('photos property is deprecated - use '
            '\'items.images()\' method.', DeprecationWarning,
            stacklevel=2)
        photos = self.items.images
        class proxy(object):
            def all(self):
                return photos()
        return proxy()


class AttachedMediaItem(models.Model):
    # Generic relation to an object.
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField()
    content_object = generic.GenericForeignKey('content_type',
        'object_id')
    
    mediaset = models.ForeignKey('media.MediaSet',
        related_name='items')
    order = models.PositiveIntegerField(default=0)
    
    objects = QuerySetManager()
    
    class QuerySet(models.query.QuerySet):
        def __init__(self, *args, **kwargs):
            # TODO: Optimisation/caching
            from thecut.media import MEDIA_SOURCE_CLASSES
            for class_ in MEDIA_SOURCE_CLASSES:
                plural_name = class_._meta.verbose_name_plural.replace(
                    ' ', '')
                content_type = ContentType.objects.get_for_model(class_)
                objects = partial(self.get_objects_for_content_type,
                    content_type=content_type)
                setattr(self, plural_name, objects)
            super(AttachedMediaItem.QuerySet, self).__init__(*args,
                **kwargs)
        
        def get_objects_for_content_type(self, content_type):
            # TODO: Optimisation/caching/queryset?
            items = self.filter(content_type=content_type)
            return [item.content_object for item in items]
    
    def __unicode__(self):
        return '%(order)s - %(model)s: %(object)s' %(
            {'order': self.order, 'model': self.content_type,
            'object': self.content_object})

