# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.files.storage import get_storage_class
from sorl.thumbnail import get_thumbnail
from thecut.media import settings


logger = get_task_logger(__name__)


@shared_task(compression='gzip', ignore_result=True, serializer='json')
def generate_thumbnail(file_name, file_storage, geometry_string, options):

    options.update({'no_placeholder': True})

    storage_import_path, storage_args, storage_kwargs = file_storage
    Storage = get_storage_class(storage_import_path)
    storage = Storage(*storage_args, **storage_kwargs)

    with storage.open(file_name) as file_:
        get_thumbnail(file_, geometry_string, **options)

    logger.info('Generated {} thumbnail for {}'.format(geometry_string,
                                                       file_name))


@shared_task(compression='gzip', ignore_result=True, serializer='json')
def generate_thumbnails(file_name, file_storage, thumbnail_sizes=None):
    thumbnails = thumbnail_sizes or settings.PREGENERATE_THUMBNAIL_SIZES

    for geometry_string, options in thumbnails:
        generate_thumbnail.delay(
            file_name=file_name, file_storage=file_storage,
            geometry_string=geometry_string, options=options)

    logger.info('Queued thumbnail generation for {}'.format(file_name))
