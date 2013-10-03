# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery.task import task
from django.contrib.contenttypes.models import ContentType


## Deprecated


@task(ignore_result=True)
def generate_thumbnail(content_type_pk, object_pk, geometry_string, options):
    """Deprecated - replaced by thecut.media.tasks.generate_thumbnail."""
    warnings.warn('This function has been replaced by ' \
                  'thecut.media.tasks.generate_thumbnail.',
                  DeprecationWarning, stacklevel=2)
    from thecut.media import tasks
    content_type = ContentType.objects.get(pk=content_type_pk)
    obj = content_type.get_object_for_this_type(pk=object_pk)
    tasks.generate_thumbnail(obj.get_image(), geometry_string, options)


@task(ignore_result=True)
def generate_thumbnails(instance, thumbnail_sizes):
    """Deprecated - replaced by thecut.media.tasks.generate_thumbnails."""
    warnings.warn('This function has been replaced by ' \
                  'thecut.media.tasks.generate_thumbnails.',
                  DeprecationWarning, stacklevel=2)
    from thecut.media import tasks
    return tasks.generate_thumbnails(instance.get_image(), thumbnail_sizes)
