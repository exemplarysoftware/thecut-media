# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import simplejson
from mimetypes import guess_type
from sorl.thumbnail import get_thumbnail
from thecut.media.mediasources import settings, utils
from thecut.media.models import AbstractMediaItem
from urllib import urlencode, urlopen
import re
import warnings


class IsProcessedMixin(object):

    @property
    def is_processed(self):
        warnings.warn('is_processed property is deprecated.',
                      DeprecationWarning, stacklevel=2)
        return True

    @is_processed.setter
    def is_processed(self, value):
        warnings.warn('is_processed property is deprecated.',
                      DeprecationWarning, stacklevel=2)
        pass


class AbstractDocument(IsProcessedMixin, AbstractMediaItem):

    file = models.FileField(max_length=250,
                            upload_to='uploads/media/documents/%Y/%m/%d')

    class Meta(AbstractMediaItem.Meta):
        abstract = True

    def clean(self, *args, **kwargs):
        super(AbstractDocument, self).clean(*args, **kwargs)
        if not 'file' in kwargs.get('exclude', []):
            length = len(self.file.field.generate_filename(
                self, self.file.name))
            if length > self.file.field.max_length:
                raise ValidationError(
                    'Document filename is too long, please rename the file to '
                    'a shorter name before uploading.')

    def get_absolute_url(self):
        return self.file.url

    def get_filename(self):
        return self.file.name.split('/')[-1]

    def get_image(self, no_placeholder=False):
        if no_placeholder:
            warnings.warn('no_placeholder argument is deprecated.',
                          DeprecationWarning, stacklevel=2)
        if self.file:
            try:
                image = get_thumbnail(self.file, '1000x1000', upscale=False)
            except:
                image = None
            return image
        else:
            return utils.get_placeholder_image()

    def get_mime_type(self):
        mime = guess_type(self.file.path)
        return mime[0] if mime else None

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                existing = self.__class__.objects.get(pk=self.pk)
            except self.__class__.DoesNotExist:
                pass
            else:
                if existing.file != self.file:
                    utils.delete_file(self.__class__, existing)
        return super(AbstractDocument, self).save(*args, **kwargs)


class Document(AbstractDocument):

    pass

models.signals.post_save.connect(utils.generate_thumbnails, sender=Document)
models.signals.pre_delete.connect(utils.delete_file, sender=Document)


class AbstractImage(IsProcessedMixin, AbstractMediaItem):

    file = models.ImageField(max_length=250,
                             upload_to='uploads/media/images/%Y/%m/%d')

    class Meta(AbstractMediaItem.Meta):
        abstract = True

    def clean(self, *args, **kwargs):
        super(AbstractImage, self).clean(*args, **kwargs)
        if not 'file' in kwargs.get('exclude', []):
            length = len(self.file.field.generate_filename(
                self, self.file.name))
            if length > self.file.field.max_length:
                raise ValidationError(
                    'Image filename is too long, please rename the file to a '
                    'shorter name before uploading.')

    def get_absolute_url(self):
        return self.file.url

    def get_filename(self):
        return self.file.name.split('/')[-1]

    def get_image(self, no_placeholder=False):
        if no_placeholder:
            warnings.warn('no_placeholder argument is deprecated.',
                          DeprecationWarning, stacklevel=2)
        return self.file

    def get_mime_type(self):
        mime = guess_type(self.file.path)
        return mime[0] if mime else None

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                existing = self.__class__.objects.get(pk=self.pk)
            except self.__class__.DoesNotExist:
                pass
            else:
                if existing.file != self.file:
                    utils.delete_file(self.__class__, existing)
        return super(AbstractImage, self).save(*args, **kwargs)


class Image(AbstractImage):

    pass

models.signals.post_save.connect(utils.generate_thumbnails, sender=Image)
models.signals.pre_delete.connect(utils.delete_file, sender=Image)


class AbstractVideo(IsProcessedMixin, AbstractMediaItem):

    file = models.FileField(max_length=250,
                            upload_to='uploads/media/videos/%Y/%m/%d')
    #image = models.ImageField(max_length=250,
    #                          upload_to='uploads/media/videos/%Y/%m/%d',
    #                          blank=True, default='')

    class Meta(AbstractMediaItem.Meta):
        abstract = True

    def clean(self, *args, **kwargs):
        super(AbstractVideo, self).clean(*args, **kwargs)
        if not 'file' in kwargs.get('exclude', []):
            length = len(self.file.field.generate_filename(
                self, self.file.name))
            if length > self.file.field.max_length:
                raise ValidationError(
                    'Video filename is too long, please rename the file to a '
                    'shorter name before uploading.')

    def get_absolute_url(self):
        return self.file.url

    def get_filename(self):
        return self.file.name.split('/')[-1]

    #def get_image(self):
    #    return self.file

    def get_mime_type(self):
        mime = guess_type(self.file.path)
        return mime[0] if mime else None

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

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                existing = self.__class__.objects.get(pk=self.pk)
            except self.__class__.DoesNotExist:
                pass
            else:
                if existing.file != self.file:
                    utils.delete_file(self.__class__, existing)
        return super(AbstractVideo, self).save(*args, **kwargs)


class Video(AbstractVideo):

    pass

models.signals.post_save.connect(utils.generate_thumbnails, sender=Video)
models.signals.pre_delete.connect(utils.delete_file, sender=Video)


class AbstractYoutubeVideo(IsProcessedMixin, AbstractMediaItem):

    url = models.URLField()

    class Meta(AbstractMediaItem.Meta):
        abstract = True

    def get_absolute_url(self):
        return 'http://www.youtube.com/watch?v={video_id}'.format(
            video_id=self.get_video_id())

    def get_image(self, no_placeholder=False):
        if no_placeholder:
            warnings.warn('no_placeholder argument is deprecated.',
                          DeprecationWarning, stacklevel=2)
        return 'http://img.youtube.com/vi/{video_id}/0.jpg'.format(
            video_id=self.get_video_id())

    def get_video_id(self):
        match = re.match(r'https?://youtu.be/([-a-z0-9A-Z_]+)$', self.url)
        if not match:
            match = re.match(
                r'^https?://www.youtube.com/watch\?v=([-a-z0-9A-Z_]+)(?:&{,1}.*)$',
                self.url)
        if match:
            return match.groups()[0]


class YoutubeVideo(AbstractYoutubeVideo):

    pass

models.signals.post_save.connect(utils.generate_thumbnails,
                                 sender=YoutubeVideo)


class AbstractVimeoVideo(IsProcessedMixin, AbstractMediaItem):

    url = models.URLField(help_text='e.g. http://vimeo.com/123456')
    _api_data = models.TextField(blank=True, default='', editable=False)
    _oembed_data = models.TextField(blank=True, default='', editable=False)

    class Meta(AbstractMediaItem.Meta):
        abstract = True

    def get_absolute_url(self):
        return self.url

    def get_image(self, no_placeholder=False):
        if no_placeholder:
            warnings.warn('no_placeholder argument is deprecated.',
                          DeprecationWarning, stacklevel=2)
        return self.api_data['thumbnail_large']

    @property
    def api_data(self):
        if not self._api_data:
            self._api_data = self._get_api_data()
        return simplejson.loads(self._api_data)[0]

    def _get_api_data(self):
        base_uri = 'http://vimeo.com/api/v2/'
        video_uri = '{0}video/{1}.json'.format(base_uri, self.get_video_id())
        response = urlopen(video_uri)
        return response.read()

    @property
    def oembed_data(self):
        if not self._oembed_data:
             self._oembed_data = self._get_oembed_data()
        return simplejson.loads(self._oembed_data)

    def _get_oembed_data(self):
        params = urlencode({'url': self.url})
        uri = 'http://vimeo.com/api/oembed.json?{0}'.format(params)
        response = urlopen(uri)
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

    pass

models.signals.post_save.connect(utils.generate_thumbnails, sender=VimeoVideo)


class AbstractAudio(IsProcessedMixin, AbstractMediaItem):

    file = models.FileField(max_length=250,
                            upload_to='uploads/media/audios/%Y/%m/%d')

    class Meta(AbstractMediaItem.Meta):
        abstract = True

    def clean(self, *args, **kwargs):
        super(AbstractAudio, self).clean(*args, **kwargs)
        if not 'file' in kwargs.get('exclude', []):
            length = len(self.file.field.generate_filename(self,
                self.file.name))
            if length > self.file.field.max_length:
                raise ValidationError(
                    'Audio filename is too long, please rename the file to a '
                    'shorter name before uploading.')

    def get_absolute_url(self):
        return self.file.url

    def get_filename(self):
        return self.file.name.split('/')[-1]

    def get_mime_type(self):
        mime = guess_type(self.file.path)
        return mime[0] if mime else None

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                existing = self.__class__.objects.get(pk=self.pk)
            except self.__class__.DoesNotExist:
                pass
            else:
                if existing.file != self.file:
                    utils.delete_file(self.__class__, existing)
        return super(AbstractAudio, self).save(*args, **kwargs)


class Audio(AbstractAudio):

    pass

models.signals.pre_delete.connect(utils.delete_file, sender=Audio)
