# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.files.uploadedfile import TemporaryUploadedFile
from django.utils._os import upath
from magic import Magic
from thecut.media.mediasources import settings
import os


def generate_thumbnails(sender, instance, created, raw=False, **kwargs):
    if created and settings.QUEUE_THUMBNAILS and not raw:
        from thecut.media import tasks

        file_ = instance.get_image(no_placeholder=True)

        # TODO - still required? no longer pickling.
        # Workaround for LazyStorage / LazyObject, which can't be pickled
        if hasattr(file_, 'storage') \
                and hasattr(file_.storage, '_wrapped') \
                and hasattr(file_.storage, '_setup'):
            file_.storage._setup()
            file_.storage = file_.storage._wrapped

        tasks.generate_thumbnails.delay(
            file_name=file_.name, file_storage=file_.storage.deconstruct())


def delete_file(sender, instance, **kwargs):
    from sorl.thumbnail import delete
    delete(instance.file)


def get_content_type(uploaded_file):
    """Get the content type of an uploaded file."""

    if uploaded_file.name[-5:].lower() == '.docx' or \
       uploaded_file.name[-5:].lower() == '.xlsx' or \
       uploaded_file.name[-5:].lower() == '.pptx':
            msooxml_magic_file = os.path.join(
                os.path.dirname(os.path.realpath(upath(__file__))),
                'magic/msooxml.magic')
    else:
        msooxml_magic_file = None
    magic = Magic(mime=True, magic_file=msooxml_magic_file)
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
