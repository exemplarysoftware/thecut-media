# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from thecut.media.mediasources import settings


def get_placeholder_image():
    from django.core.files.images import ImageFile
    if settings.STATICFILES_STORAGE:
        from django.core.files.storage import get_storage_class
        storage_class = get_storage_class(settings.STATICFILES_STORAGE)
        storage = storage_class()
        placeholder = storage.open(settings.PLACEHOLDER_IMAGE_PATH)
        image = ImageFile(placeholder)
        image.storage = storage
    else:
        placeholder = open('%s/%s' %(settings.STATIC_ROOT,
            settings.PLACEHOLDER_IMAGE_PATH))
        image = ImageFile(placeholder)
    return image


def generate_thumbnails(instance, thumbnail_sizes):
    """Queue tasks to generate required thumbnails."""
    from thecut.media.mediasources import tasks
    tasks.generate_thumbnails.delay(instance, thumbnail_sizes)


def generate_image_thumbnails(sender, instance, created, **kwargs):
    if not instance.is_processed and settings.GENERATE_THUMBNAILS_ON_SAVE:
        generate_thumbnails(instance, settings.IMAGE_THUMBNAILS)


def generate_document_thumbnails(sender, instance, created, **kwargs):
    if not instance.is_processed and settings.GENERATE_THUMBNAILS_ON_SAVE:
        generate_thumbnails(instance, settings.DOCUMENT_THUMBNAILS)


def generate_video_thumbnails(sender, instance, created, **kwargs):
    if not instance.is_processed and settings.GENERATE_THUMBNAILS_ON_SAVE:
        generate_thumbnails(instance, settings.VIDEO_THUMBNAILS)


def generate_youtube_video_thumbnails(sender, instance, created, **kwargs):
    if not instance.is_processed and settings.GENERATE_THUMBNAILS_ON_SAVE:
        generate_thumbnails(instance, settings.YOUTUBE_VIDEO_THUMBNAILS)


def generate_vimeo_video_thumbnails(sender, instance, created, **kwargs):
    if not instance.is_processed and settings.GENERATE_THUMBNAILS_ON_SAVE:
        generate_thumbnails(instance, settings.VIMEO_VIDEO_THUMBNAILS)


def delete_file(sender, instance, **kwargs):
    from sorl.thumbnail import delete
    delete(instance.file)

