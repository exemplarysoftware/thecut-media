# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import simplejson
from mimetypes import guess_type
from sorl.thumbnail import get_thumbnail
from thecut.core.managers import QuerySetManager
from thecut.media.mediasources import utils
from thecut.media.models import AbstractMediaItem
from urllib import urlencode, urlopen
import re
import warnings


class AbstractDocument(AbstractMediaItem):
    file = models.FileField(max_length=250,
        upload_to='uploads/media/documents/%Y/%m/%d')
    objects = QuerySetManager()
    
    class Meta(AbstractMediaItem.Meta):
        abstract = True
    
    def clean(self, *args, **kwargs):
        super(AbstractDocument, self).clean(*args, **kwargs)
        if not 'file' in kwargs.get('exclude', []):
            length = len(self.file.field.generate_filename(self,
                self.file.name))
            if length > self.file.field.max_length:
                raise ValidationError('Document filename is too long, ' \
                    'please rename the file to a shorter name before ' \
                    'uploading.')
    
    def get_absolute_url(self):
        return self.file.url
    
    def get_image(self):
        try:
            image = get_thumbnail(self.file, '1000x1000', upscale=False)
        except:
            image = None
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


class Document(AbstractDocument):
    objects = QuerySetManager()


class AbstractImage(AbstractMediaItem):
    file = models.ImageField(max_length=250,
        upload_to='uploads/media/images/%Y/%m/%d')
    objects = QuerySetManager()
    
    class Meta(AbstractMediaItem.Meta):
        abstract = True
    
    def clean(self, *args, **kwargs):
        super(AbstractImage, self).clean(*args, **kwargs)
        if not 'file' in kwargs.get('exclude', []):
            length = len(self.file.field.generate_filename(self,
                self.file.name))
            if length > self.file.field.max_length:
                raise ValidationError('Image filename is too long, please ' \
                    'rename the file to a shorter name before uploading.')
    
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


class Image(AbstractImage):
    objects = QuerySetManager()

models.signals.post_save.connect(utils.generate_image_thumbnails,
    sender=Image)


class AbstractVideo(AbstractMediaItem):
    file = models.FileField(max_length=250,
        upload_to='uploads/media/videos/%Y/%m/%d')
    #image = models.ImageField(
    #    upload_to='uploads/media/videos/%Y/%m/%d',
    #    blank=True, null=True)
    objects = QuerySetManager()
    
    class Meta(AbstractMediaItem.Meta):
        abstract = True
    
    def clean(self, *args, **kwargs):
        super(AbstractVideo, self).clean(*args, **kwargs)
        if not 'file' in kwargs.get('exclude', []):
            length = len(self.file.field.generate_filename(self,
                self.file.name))
            if length > self.file.field.max_length:
                raise ValidationError('Video filename is too long, please ' \
                    'rename the file to a shorter name before uploading.')
    
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


class Video(AbstractVideo):
    objects = QuerySetManager()

models.signals.post_save.connect(utils.generate_video_thumbnails,
    sender=Video)


class AbstractYoutubeVideo(AbstractMediaItem):
    url = models.URLField()
    objects = QuerySetManager()
    
    class Meta(AbstractMediaItem.Meta):
        abstract = True
    
    def get_absolute_url(self):
        return 'http://www.youtube.com/watch?v=%(video_id)s' %(
            {'video_id': self.get_video_id()})
    
    def get_image(self):
        return 'http://img.youtube.com/vi/%(video_id)s/0.jpg' %(
            {'video_id': self.get_video_id()})
    
    def get_video_id(self):
        match = re.match(r'http://youtu.be/([-a-z0-9A-Z_]+)$', self.url)
        if not match:
            match = re.match(
                r'^http://www.youtube.com/watch\?v=([-a-z0-9A-Z_]+)(?:&{,1}.*)$',
                self.url)
        if match:
            return match.groups()[0]


class YoutubeVideo(AbstractYoutubeVideo):
    objects = QuerySetManager()

models.signals.post_save.connect(utils.generate_youtube_video_thumbnails,
    sender=YoutubeVideo)


class AbstractVimeoVideo(AbstractMediaItem):
    url = models.URLField(help_text='e.g. http://vimeo.com/123456')
    objects = QuerySetManager()
    _api_data = models.TextField(blank=True, null=True, editable=False)
    _oembed_data = models.TextField(blank=True, null=True, editable=False)
    
    class Meta(AbstractMediaItem.Meta):
        abstract = True
    
    def get_absolute_url(self):
        return self.file.url
    
    def get_image(self):
        return self.api_data['thumbnail_large']
    
    @property
    def api_data(self):
        if not self._api_data:
            self._api_data = self._get_api_data()
        return simplejson.loads(self._api_data)[0]
    
    def _get_api_data(self):
        base_uri = 'http://vimeo.com/api/v2/'
        video_uri = '%svideo/%s.json' %(base_uri, self.get_video_id())
        response = urlopen(video_uri)
        return response.read()
    
    @property
    def oembed_data(self):
        if not self._oembed_data:
             self._oembed_data = self._get_oembed_data()
        return simplejson.loads(self._oembed_data)
    
    def _get_oembed_data(self):
        base_uri = 'http://vimeo.com/api/oembed.json'
        params = urlencode({'url': self.url})
        response = urlopen(base_uri, params)
        return response.read()
    
    def get_video_id(self):
        url_pattern = re.compile(r'vimeo.com\/(\d+)\/?')
        match = re.search(url_pattern, self.url)
        return match and match.groups()[0] or None
    
    def html(self):
        return self.oembed_data['html']
    
    def save(self, *args, **kwargs):
        if not self.pk:
            data = self.api_data
            self.title = self.title or data['title']
            self.content = self.content or data['description']
        if not self._oembed_data:
            self._get_oembed_data()
        return super(AbstractVimeoVideo, self).save(*args, **kwargs)


class VimeoVideo(AbstractVimeoVideo):
    objects = QuerySetManager()

models.signals.post_save.connect(utils.generate_vimeo_video_thumbnails,
    sender=VimeoVideo)


class AbstractAudio(AbstractMediaItem):
    file = models.FileField(max_length=250,
        upload_to='uploads/media/audios/%Y/%m/%d')
    objects = QuerySetManager()
    
    class Meta(AbstractMediaItem.Meta):
        abstract = True
    
    def clean(self, *args, **kwargs):
        super(AbstractAudio, self).clean(*args, **kwargs)
        if not 'file' in kwargs.get('exclude', []):
            length = len(self.file.field.generate_filename(self,
                self.file.name))
            if length > self.file.field.max_length:
                raise ValidationError('Audio filename is too long, please ' \
                    'rename the file to a shorter name before uploading.')
    
    def get_absolute_url(self):
        return self.file.url
    
    def get_mime_type(self):
        return guess_type(self.file.path)[0]


class Audio(AbstractAudio):
    objects = QuerySetManager()

