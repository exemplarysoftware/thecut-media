# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.files.uploadedfile import TemporaryUploadedFile
from thecut.media import utils as media_utils
from thecut.media.mediasources import settings
import warnings


def get_placeholder_image(*args, **kwargs):
    """Deprecated - moved to thecut.media.utils."""
    warnings.warn('This function has been moved to thecut.media.utils.',
                  DeprecationWarning, stacklevel=2)
    return media_utils.get_placeholder_image(*args, **kwargs)


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


def get_metadata(uploaded_file):
    """Get metadata for an uploaded file."""
    from exiftool import ExifTool

    # If we are not dealing with a TemporaryUploadedFile (such as
    # InMemoryUploadedFile), create a TemporaryUploadedFile.
    if not isinstance(uploaded_file, TemporaryUploadedFile):
        temp_file = TemporaryUploadedFile(
            name=uploaded_file.name, content_type=uploaded_file.content_type,
            size=uploaded_file.size, charset=uploaded_file.charset)
        uploaded_file.seek(0)
        temp_file.write(uploaded_file.read())
        uploaded_file.seek(0)
    else:
        temp_file = uploaded_file

    with ExifTool() as et:
        metadata = et.get_metadata(temp_file.temporary_file_path())

    return metadata
