# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import content_types, utils
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail
from thecut.media.models import AbstractMediaItem
import codecs
import json
import re

try:
    from urllib.parse import urlencode
    from urllib.request import urlopen
except ImportError:  # Python 2
    from urllib import urlencode, urlopen


class FileFieldLengthMixin(object):

    def clean(self, *args, **kwargs):
        super(FileFieldLengthMixin, self).clean(*args, **kwargs)

        # Check file names against lengths
        for field in self._meta.fields:
            if field.name not in kwargs.get('exclude', []) and \
                    isinstance(field, models.FileField):
                bound_field = getattr(self, field.name)
                length = len(field.generate_filename(self, bound_field.name))
                if length > field.max_length:
                    raise ValidationError(
                        '{0} name is too long. Rename the file to have a '
                        'shorter name before uploading.'.format(field.name))


class FileMixin(FileFieldLengthMixin, object):
    # Assumes FileField with name of 'file' on model.

    content_types = []

    def clean(self, *args, **kwargs):
        super(FileMixin, self).clean(*args, **kwargs)

        if 'file' not in kwargs.get('exclude', []) and self.file:
            content_type = self.get_content_type()
            if content_type not in self.content_types:
                raise ValidationError(
                    '"{0}" is not a supported file type.'.format(content_type))

    def get_absolute_url(self):
        return self.file.url

    def get_content_type(self):
        return utils.get_content_type(self.file)

    def get_filename(self):
        return self.file.name.split('/')[-1]

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                existing = self.__class__.objects.get(pk=self.pk)
            except self.__class__.DoesNotExist:
                pass
            else:
                if existing.file != self.file:
                    utils.delete_file(self.__class__, existing)

        if not self.title:
            self.title = '.'.join(self.get_filename().split('.')[:-1])

        return super(FileMixin, self).save(*args, **kwargs)


class AbstractDocument(FileMixin, AbstractMediaItem):

    file = models.FileField(max_length=250,
                            upload_to='uploads/media/documents/%Y/%m/%d')

    content_types = content_types.ALL_DOCUMENTS

    class Meta(AbstractMediaItem.Meta):
        abstract = True

    def get_image(self, no_placeholder=False):
        if self.file:
            try:
                image = get_thumbnail(self.file, '1000x1000', upscale=False,
                                      no_placeholder=no_placeholder)
            except:
                image = None
            return image
        else:
            return utils.get_placeholder_image()


class Document(AbstractDocument):

    pass

models.signals.post_save.connect(utils.generate_thumbnails, sender=Document)
models.signals.pre_delete.connect(utils.delete_file, sender=Document)


class AbstractImage(FileMixin, AbstractMediaItem):

    file = models.ImageField(max_length=250,
                             upload_to='uploads/media/images/%Y/%m/%d')

    content_types = content_types.IMAGE

    class Meta(AbstractMediaItem.Meta):
        abstract = True

    def get_image(self, no_placeholder=False):
        return self.file


class Image(AbstractImage):

    pass

models.signals.post_save.connect(utils.generate_thumbnails, sender=Image)
models.signals.pre_delete.connect(utils.delete_file, sender=Image)


class AbstractVideo(FileMixin, AbstractMediaItem):

    file = models.FileField(max_length=250,
                            upload_to='uploads/media/videos/%Y/%m/%d')

    content_types = content_types.VIDEO

#    image = models.ImageField(max_length=250,
#                              upload_to='uploads/media/videos/%Y/%m/%d',
#                              blank=True, default='')

    class Meta(AbstractMediaItem.Meta):
        abstract = True

#    def get_image(self, no_placeholder=False):
#        return self.file

#    def generate_image(self):
#        if self.image:
#            self.image.delete()
#        import subprocess
#        from django.conf import settings
#        #from django.core.files.images import ImageFile
#        from django.template.defaultfilters import slugify
#        file_name = slugify(self.title)
#        file_path = '%s/%s.jpg' %('uploads/videos/thumbnails', file_name)
#        command_line = 'ffmpegthumbnailer -i %s -o %s/%s -s %d' % (
#            self.file.path, settings.MEDIA_ROOT, file_path, 720)
#        subprocess.check_call(command_line, shell=True)
#        # for debugging add 'stderr=subprocess.STDOUT'
#        image = file_path #  ImageFile(open(file_path, 'rb'))
#        self.image = image
#        self.save()


class Video(AbstractVideo):

    pass

models.signals.post_save.connect(utils.generate_thumbnails, sender=Video)
models.signals.pre_delete.connect(utils.delete_file, sender=Video)


class AbstractYoutubeVideo(AbstractMediaItem):

    _oembed_data = models.TextField(blank=True, default='', editable=False)

    _url_regex = r'^https?://(?:www.youtube.com/watch\?(?:&{,1}.*)v=|' \
                 'youtu.be/)([-a-z0-9A-Z_]+)(?:&{,1}.*)$'

    url = models.URLField()

    class Meta(AbstractMediaItem.Meta):
        abstract = True

    def _get_oembed_data(self):
        params = urlencode({'url': self.url, 'format': 'json'})
        uri = 'https://www.youtube.com/oembed?{}'.format(params)
        response = urlopen(uri)
        # TODO Obtain encoding from http respsonse?
        reader = codecs.getreader('utf-8')
        return reader(response).read()

    def clean(self, *args, **kwargs):
        super(AbstractYoutubeVideo, self).clean(*args, **kwargs)

        if 'url' not in kwargs.get('exclude', []) and not re.match(
                self._url_regex, self.url):
            raise ValidationError({
                'url': ValidationError('Could not process URL. Is it a valid '
                                       'YouTube video URL?',
                                       code='invalid_url')})

    def get_absolute_url(self):
        return self.url

    def get_image(self, no_placeholder=False):
        return self.oembed_data.get('thumbnail_url')

    def get_video_id(self):
        match = re.match(self._url_regex, self.url)
        return match and match.groups()[0] or None

    def html(self):
        return mark_safe(self.oembed_data['html'])

    @property
    def oembed_data(self):
        if not self._oembed_data:
            self._oembed_data = self._get_oembed_data()
        return json.loads(self._oembed_data)

    def save(self, *args, **kwargs):
        oembed_data = self.oembed_data  # Triggers fetching json before save
        if not self.title:
            self.title = oembed_data.get('title')
        return super(AbstractYoutubeVideo, self).save(*args, **kwargs)


class YoutubeVideo(AbstractYoutubeVideo):

    pass

models.signals.post_save.connect(utils.generate_thumbnails,
                                 sender=YoutubeVideo)


class AbstractVimeoVideo(AbstractMediaItem):

    url = models.URLField(help_text='e.g. https://vimeo.com/123456')
    _api_data = models.TextField(blank=True, default='', editable=False)
    _oembed_data = models.TextField(blank=True, default='', editable=False)

    class Meta(AbstractMediaItem.Meta):
        abstract = True

    def get_absolute_url(self):
        return self.url

    def get_image(self, no_placeholder=False):
        return self.api_data['thumbnail_large']

    @property
    def api_data(self):
        if not self._api_data:
            self._api_data = self._get_api_data()
        return json.loads(self._api_data)[0]

    def _get_api_data(self):
        uri = 'https://vimeo.com/api/v2/video/{}.json'.format(
            self.get_video_id())
        response = urlopen(uri)
        return response.read()

    @property
    def oembed_data(self):
        if not self._oembed_data:
            self._oembed_data = self._get_oembed_data()
        return json.loads(self._oembed_data)

    @property
    def duration(self):
        delta = timedelta(seconds=self.api_data['duration'])
        return delta

    def _get_oembed_data(self):
        params = urlencode({'url': self.url})
        uri = 'https://vimeo.com/api/oembed.json?{}'.format(params)
        response = urlopen(uri)
        # TODO Obtain encoding from http respsonse?
        reader = codecs.getreader('utf-8')
        return reader(response).read()

    def get_video_id(self):
        url_pattern = re.compile(r'vimeo.com\/(\d+)\/?')
        match = re.search(url_pattern, self.url)
        return match and match.groups()[0] or None

    def html(self):
        return mark_safe(self.oembed_data['html'])

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


class AbstractAudio(FileMixin, AbstractMediaItem):

    file = models.FileField(max_length=250,
                            upload_to='uploads/media/audios/%Y/%m/%d')

    content_types = content_types.AUDIO

    class Meta(AbstractMediaItem.Meta):
        abstract = True


class Audio(AbstractAudio):

    pass

models.signals.pre_delete.connect(utils.delete_file, sender=Audio)
