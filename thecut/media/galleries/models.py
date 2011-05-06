from django.db import models
from thecut.core.managers import QuerySetManager
from thecut.core.models import AbstractSitesResourceWithSlug
import warnings


class Gallery(AbstractSitesResourceWithSlug):
    objects = QuerySetManager()
    
    class Meta(AbstractSitesResourceWithSlug.Meta):
        ordering = ['-publish_at', 'title']
        verbose_name_plural = 'galleries'
    
    #class QuerySet(AbstractSitesResourceWithSlug.QuerySet):
    #    def with_images(self):
    #        """Return galleries containing at least one image."""
    #        return self.annotate(
    #            num_images=models.Count('images')).filter(
    #            num_images__gte=1)
    
    @models.permalink
    def get_absolute_url(self):
        return ('galleries:gallery_media_list', [], {'slug': self.slug})
    
    ## Deprecated properties
    
    @property
    def all_images(self):
        """Deprecated - instead use 'media.images()'."""
        warnings.warn('all_images property is deprecated - use '
            '\'media.images()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.media.images()
    
    @property
    def all_photos(self):
        """Deprecated - instead use 'media.images()'."""
        warnings.warn('all_photos property is deprecated - use '
            '\'media.images()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.media.images()
    
    @property
    def image(self):
        """Deprecated - instead use 'media.get_image()'."""
        warnings.warn('image property is deprecated - use '
            '\'media.get_image()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.media.get_image()
    
    @property
    def image_order(self):
        """Deprecated. Ordering is now managed by AttachedMediaItem."""
        warnings.warn('Ordering is now managed by AttachedMediaItem '
            'model.', DeprecationWarning, stacklevel=2)
        return [image.pk for image in self.images()]
    
    @property
    def images(self):
        """Deprecated - instead use 'media.images()'."""
        warnings.warn('images property is deprecated - use '
            '\'media.images()\' method.', DeprecationWarning,
            stacklevel=2)
        images = self.media.images
        class proxy(object):
            def all(self):
                return images()
        return proxy()
    
    @property
    def ordered_images(self):
        """Deprecated - instead use 'media.images()'."""
        warnings.warn('ordered_images property is deprecated - use '
            '\'media.images()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.media.images()
    
    @property
    def photo(self):
        """Deprecated - instead use 'media.get_image()'."""
        warnings.warn('photo property is deprecated - use '
            '\'media.get_image()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.media.get_image()
    
    @property
    def photos(self):
        """Deprecated - instead use 'media.images()'."""
        warnings.warn('photos property is deprecated - use '
            '\'media.images()\' method.', DeprecationWarning,
            stacklevel=2)
        photos = self.media.images
        class proxy(object):
            def all(self):
                return photos()
        return proxy()

