# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.contenttypes.models import ContentType
from thecut.media.mediasources import settings


def generate_thumbnails(instance, thumbnail_sizes):
    """Queue tasks to generate required thumbnails."""
    from thecut.media.mediasources import tasks
    content_type = ContentType.objects.get_for_model(instance)
    for geometry_string, options in thumbnail_sizes:
        tasks.generate_thumbnail.delay(content_type.pk, instance.pk,
            geometry_string, options)


def generate_image_thumbnails(sender, instance, created, **kwargs):
    if settings.CELERY:
        generate_thumbnails(instance, settings.IMAGE_THUMBNAILS)


def generate_video_thumbnails(sender, instance, created, **kwargs):
    if settings.CELERY:
        generate_thumbnails(instance, settings.VIDEO_THUMBNAILS)


def generate_youtube_video_thumbnails(sender, instance, created, **kwargs):
    if settings.CELERY:
        generate_thumbnails(instance, settings.YOUTUBE_VIDEO_THUMBNAILS)


def generate_vimeo_video_thumbnails(sender, instance, created, **kwargs):
    if settings.CELERY:
        generate_thumbnails(instance, settings.VIMEO_VIDEO_THUMBNAILS)

