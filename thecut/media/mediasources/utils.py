# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from thecut.media.mediasources import settings


def get_placeholder_image():
    # TODO: Fetch from staticfiles storage
    from django.core.files.images import ImageFile
    f = open(settings.PLACEHOLDER_IMAGE_PATH)
    return ImageFile(f)


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

