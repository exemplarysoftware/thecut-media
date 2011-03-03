from django.db import models
from mimetypes import guess_type
from sorl.thumbnail import get_thumbnail
from thecut.core.managers import QuerySetManager
from thecut.media.models import AbstractMediaItem
import re
import warnings


class Document(AbstractMediaItem):
    file = models.FileField(
        upload_to='uploads/media/documents/%Y/%m/%d')
    objects = QuerySetManager()
    
    def get_absolute_url(self):
        return self.file.url
    
    def get_image(self):
        image = get_thumbnail(self.file, '1000x1000', upscale=False)
        return image
    
    def get_mime_type(self):
        return guess_type(self.file.path)[0]
    
    ## Deprecated properties
    
    @property
    def mime_type(self):
        """Deprecated - instead use 'get_mime_type()'."""
        warnings.warn('mime_type property is deprecated - use '
            '\'get_mime_type()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.get_mime_type()


class Image(AbstractMediaItem):
    file = models.ImageField(
        upload_to='uploads/media/images/%Y/%m/%d')
    objects = QuerySetManager()
    
    def get_absolute_url(self):
        return self.file.url
    
    def get_image(self):
        return self.file
    
    def get_mime_type(self):
        return guess_type(self.file.path)[0]
    
    ## Deprecated properties
    
    @property
    def get_display_url(self):
        """Deprecated - instead use 'get_absolute_url'."""
        # For backwards compatibility, set the commonly used
        # 'get_display_url' property which is used in other apps
        # default templates.
        warnings.warn('Deprecated - use \'get_absolute_url\' '
            'property.', DeprecationWarning, stacklevel=2)
        return self.get_absolute_url()
    
    @property
    def image(self):
        """Deprecated - instead use 'file'."""
        warnings.warn('Deprecated - use \'file\' property.',
            DeprecationWarning, stacklevel=2)
        return self.file
    
    @property
    def mime_type(self):
        """Deprecated - instead use 'get_mime_type()'."""
        warnings.warn('mime_type property is deprecated - use '
            '\'get_mime_type()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.get_mime_type()


class Video(AbstractMediaItem):
    file = models.FileField(
        upload_to='uploads/media/videos/%Y/%m/%d')
    #image = models.ImageField(
    #    upload_to='uploads/media/videos/%Y/%m/%d',
    #    blank=True, null=True)
    objects = QuerySetManager()
    
    def get_absolute_url(self):
        return self.file.url
    
    #def get_image(self):
    #    return self.image
    
    def get_mime_type(self):
        return guess_type(self.file.path)[0]
    
    #def generate_image(self):
    #    if self.image:
    #        self.image.delete()
    #    import subprocess
    #    from django.conf import settings
    #    #from django.core.files.images import ImageFile
    #    from django.template.defaultfilters import slugify
    #    file_name = slugify(self.title)
    #    file_path = '%s/%s.jpg' %('uploads/videos/thumbnails', file_name)
    #    command_line = 'ffmpegthumbnailer -i %s -o %s/%s -s %d' % (self.file.path, settings.MEDIA_ROOT, file_path, 720)
    #    subprocess.check_call(command_line, shell=True)#, stderr=subprocess.STDOUT)
    #    image = file_path#ImageFile(open(file_path, 'rb'))
    #    self.image = image
    #    self.save()
    
    ## Deprecated properties
    
    @property
    def mime_type(self):
        """Deprecated - instead use 'get_mime_type()'."""
        warnings.warn('mime_type property is deprecated - use '
            '\'get_mime_type()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.get_mime_type()


class YoutubeVideo(AbstractMediaItem):
    url = models.URLField()
    objects = QuerySetManager()
    
    def get_absolute_url(self):
        return self.url
    
    def get_image(self):
        return 'http://img.youtube.com/vi/%(video_id)s/0.jpg' %(
            {'video_id': self.get_video_id()})
    
    def get_video_id(self):
        url_pattern = re.compile(
            r'^http://www.youtube.com/watch\?v=([-a-z0-9A-Z_]+)$')
        match = re.match(url_pattern, self.url)
        if match:
            return match.groups()[0]

