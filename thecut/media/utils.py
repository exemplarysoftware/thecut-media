# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.contenttypes.models import ContentType
from django.core.files.images import ImageFile
from django.db.models import get_models
from thecut.media import settings


def get_media_source_classes(model_list=None):
    """Returns classes for the each string in list."""
    from thecut.media.models import AbstractMediaItem
    model_list = model_list or settings.MEDIA_SOURCES
    source_classes = []
    for import_string in model_list:
        module_string = '.'.join(import_string.split('.')[:-1])
        class_string = import_string.split('.')[-1]
        module = __import__(module_string, globals(), locals(), [class_string])
        class_ = getattr(module, class_string)
        if issubclass(class_, AbstractMediaItem):
            source_classes += [class_]
    return source_classes


def get_media_source_models():
    """Returns list of models which subclass AbstractMediaItem."""
    from thecut.media.models import AbstractMediaItem
    return [model for model in get_models() if issubclass(
            model, AbstractMediaItem)]


def get_media_source_content_types():
    """Returns list of tuples containing model and content type."""
    return [(model, ContentType.objects.get_for_model(model)) for model in \
            get_media_source_models()]


def get_placeholder_image():
    if settings.STATICFILES_STORAGE:
        from django.core.files.storage import get_storage_class
        storage_class = get_storage_class(settings.STATICFILES_STORAGE)
        storage = storage_class()
        placeholder = storage.open(settings.PLACEHOLDER_IMAGE_PATH)
        image = ImageFile(placeholder)
        image.storage = storage
    else:
        placeholder = open('{0}/{1}'.format(settings.STATIC_ROOT,
                                            settings.PLACEHOLDER_IMAGE_PATH))
        image = ImageFile(placeholder)
    return image
