# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.files.uploadedfile import TemporaryUploadedFile
from magic import Magic
from thecut.media import utils as media_utils
from thecut.media.mediasources import settings
import warnings
import os
from django.utils._os import upath


def generate_thumbnails(sender, instance, created, **kwargs):
    if created and settings.QUEUE_THUMBNAILS:
        from thecut.media import tasks
        tasks.generate_thumbnails(instance.get_image(no_placeholder=True))


def delete_file(sender, instance, **kwargs):
    from sorl.thumbnail import delete
    delete(instance.file)


def get_content_type(uploaded_file):
    """Get the content type of an uploaded file."""

    msooxml_magic_file = os.path.join(
        os.path.dirname(os.path.realpath(upath(__file__))), 'msooxml.magic')
    magic = Magic(mime=True, mime_file=msooxml_magic_file)
    uploaded_file.seek(0)
    content_type = magic.from_buffer(uploaded_file.read(
        settings.MEDIASOURCES_MAGIC_BUFFER_SIZE))
    uploaded_file.seek(0)
    return content_type


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


# Deprecated functions


def get_placeholder_image(*args, **kwargs):
    """Deprecated - moved to thecut.media.utils."""
    warnings.warn('This function has been moved to thecut.media.utils.',
                  DeprecationWarning, stacklevel=2)
    return media_utils.get_placeholder_image(*args, **kwargs)


def generate_image_thumbnails(sender, instance, created, **kwargs):
    """Deprecated - replaced by generate_thumbnails."""
    warnings.warn('This function has been replaced by generate_thumbnails.',
                  DeprecationWarning, stacklevel=2)
    return generate_thumbnails(sender, instance, created, **kwargs)


def generate_document_thumbnails(sender, instance, created, **kwargs):
    """Deprecated - replaced by generate_thumbnails."""
    warnings.warn('This function has been replaced by generate_thumbnails.',
                  DeprecationWarning, stacklevel=2)
    return generate_thumbnails(sender, instance, created, **kwargs)


def generate_video_thumbnails(sender, instance, created, **kwargs):
    """Deprecated - replaced by generate_thumbnails."""
    warnings.warn('This function has been replaced by generate_thumbnails.',
                  DeprecationWarning, stacklevel=2)
    return generate_thumbnails(sender, instance, created, **kwargs)


def generate_youtube_video_thumbnails(sender, instance, created, **kwargs):
    """Deprecated - replaced by generate_thumbnails."""
    warnings.warn('This function has been replaced by generate_thumbnails.',
                  DeprecationWarning, stacklevel=2)
    return generate_thumbnails(sender, instance, created, **kwargs)


def generate_vimeo_video_thumbnails(sender, instance, created, **kwargs):
    """Deprecated - replaced by generate_thumbnails."""
    warnings.warn('This function has been replaced by generate_thumbnails.',
                  DeprecationWarning, stacklevel=2)
    return generate_thumbnails(sender, instance, created, **kwargs)
