# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery.task import task
from sorl.thumbnail import get_thumbnail
from thecut.media import settings


@task(ignore_result=True)
def generate_thumbnail(file_, geometry_string, options):
    logger = generate_thumbnail.get_logger()
    options.update({'no_placeholder': True})
    thumbnail = get_thumbnail(file_, geometry_string, **options)
    logger.info('Generated {0} thumbnail for {1}'.format(geometry_string,
                                                         file_))


@task(ignore_result=True)
def generate_thumbnails(file_, thumbnail_sizes=None):
    logger = generate_thumbnail.get_logger()
    thumbnails = thumbnail_sizes or settings.PREGENERATE_THUMBNAIL_SIZES
    for geometry_string, options in thumbnails:
        try:
            generate_thumbnail.delay(file_, geometry_string, options)
        except:
            pass
    logger.info('Queued thumbnail generation for {0}'.format(file_))
