# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import settings
from django.core.files.images import ImageFile
from django.apps import apps
from django.template import engines
from sorl.thumbnail import get_thumbnail
import itertools
import os
import re
import warnings


def find_thumbnails_in_templates():
    """Returns a list of thumbnail geometries/options found in templates.
    Experimental."""
    loaders = itertools.chain(*[e.engine.get_template_loaders(e.engine.loaders)
                                for e in engines.all()])

    paths = set()

    for loader in loaders:
        paths.update(loader.get_template_sources(''))

    templates = set()

    for path in paths:
        for root, dirs, files in os.walk(path):
            templates.update(os.path.join(root, name) for name in files)

    pattern = re.compile(
        r'{%\s*thumbnail\s+[\w\.]+\s([\w\s\."=]*) as [\w]*\s*%}',
        flags=re.IGNORECASE)

    matches = set()

    for template in templates:
        with open(template, 'r') as f:
            for match in pattern.finditer(f.read()):
                matches.add(match.group(1))

    output = []

    for match in sorted(matches):
        parts = match.split()
        geometry_size, options = parts[0].strip('"'), parts[1:]
        options = dict([i.split('=') for i in options])
        if 'crop' in options.keys():
            options.update({'crop': options['crop'].strip('"')})
        if 'quality' in options.keys():
            options.update({'quality': int(options['quality'])})
        output += [(geometry_size, options)]

    return output


def get_media_source_models():
    """Returns list of models which subclass AbstractMediaItem."""
    from .models import AbstractMediaItem
    return [model for model in apps.get_models() if issubclass(
            model, AbstractMediaItem)]


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


def get_preview_thumbnail(image):
    geometry_size = settings.DEFAULT_ADMIN_THUMBNAIL_SIZE[0]
    options = settings.DEFAULT_ADMIN_THUMBNAIL_SIZE[1]
    return get_thumbnail(image, geometry_size, **options)


def queue_thumbnails():
    """Queue thumbnail generation for all media instances with a ``get_image``
    method."""
    from .models import MediaContentType
    from .tasks import generate_thumbnails

    # Note, using iterator here as a workaround for bug #7241
    for contenttype in MediaContentType.objects.all().iterator():
        model_class = contenttype.model_class()
        if hasattr(model_class, 'get_image'):
            for mediaitem in model_class.objects.all():
                generate_thumbnails(mediaitem.get_image())


def get_media_source_content_types():
    """Deprecated method. Use MediaContentType.objects.

    Returns list of tuples containing model and content type.

    """

    warnings.warn('get_media_source_content_types is deprecated. Use '
                  'MediaContentType.objects.', DeprecationWarning,
                  stacklevel=2)
    from .models import MediaContentType
    return [(content_type.model_class(), content_type) for content_type
            in MediaContentType.objects.all()]


# USED FOR DEBUGGING
# FROM http://stackoverflow.com/a/23874019

def show_urls(urllist, depth=0):
    for entry in urllist:
        print("  " * depth, entry.regex.pattern)
        if hasattr(entry, 'url_patterns'):
            show_urls(entry.url_patterns, depth + 1)

