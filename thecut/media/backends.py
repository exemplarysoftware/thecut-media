# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from sorl.thumbnail import base, default
from sorl.thumbnail.conf import (settings as thumbnail_settings,
                                 defaults as thumbnail_defaults)
from sorl.thumbnail.images import ImageFile
from thecut.media import settings, tasks, utils
import six


class ThumbnailBackend(base.ThumbnailBackend):

    def get_thumbnail(self, file_, geometry_string, **options):

        no_placeholder = options.pop('no_placeholder', False)
        if no_placeholder or not settings.QUEUE_THUMBNAILS:
            # Return the get_thumbnail method from standard backend.
            return super(ThumbnailBackend, self).get_thumbnail(
                file_, geometry_string, **options)

        for key, value in six.iteritems(self.default_options):
            options.setdefault(key, value)

        for key, attr in self.extra_options:
            value = getattr(thumbnail_settings, attr)
            if value != getattr(thumbnail_defaults, attr):
                options.setdefault(key, value)

        source = ImageFile(file_)
        name = self._get_thumbnail_filename(source, geometry_string, options)
        thumbnail = ImageFile(name, default.storage)
        cached = default.kvstore.get(thumbnail)

        if cached:
            return cached

        else:
            # Queue thumbnail generation, and return placeholder
            default.kvstore.delete(thumbnail, delete_thumbnails=False)
            # Workaround for LazyStorage / LazyObject, which can't be pickled
            if hasattr(file_, 'storage') \
                    and hasattr(file_.storage, '_wrapped') \
                    and hasattr(file_.storage, '_setup'):
                file_.storage._setup()
                file_.storage = file_.storage._wrapped
            tasks.generate_thumbnail.delay(file_, geometry_string, options)
            placeholder = utils.get_placeholder_image()
            return super(ThumbnailBackend, self).get_thumbnail(
                placeholder, geometry_string, **options)
