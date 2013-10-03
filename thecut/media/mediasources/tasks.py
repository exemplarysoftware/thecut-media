# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery.task import task
from django.contrib.contenttypes.models import ContentType
from sorl.thumbnail import get_thumbnail


@task(ignore_result=True)
def generate_thumbnail(content_type_pk, object_pk, geometry_string, options):
    logger = generate_thumbnail.get_logger()
    content_type = ContentType.objects.get(pk=content_type_pk)
    obj = content_type.get_object_for_this_type(pk=object_pk)
    get_thumbnail(obj.get_image(no_placeholder=True), geometry_string,
                  **options)
    logger.info('Generated {0} thumbnail for {0}'.format(geometry_string, obj))

#@task(ignore_result=True)
#def generate_thumbnail(content_type_pk, object_pk, geometry_string, options):
#    """Deprecated - moved to thecut.media.tasks."""
#    warnings.warn('This function has been moved to thecut.media.tasks.',
#                  DeprecationWarning, stacklevel=2)
#    from thecut.media import tasks as media_tasks
#    media_tasks.generate_thumbnail(content_type_pk, object_pk, geometry_string,
#                                   options)


@task(ignore_result=True)
def generate_thumbnails(instance, thumbnail_sizes):
    logger = generate_thumbnail.get_logger()
    content_type = ContentType.objects.get_for_model(instance)
    for geometry_string, options in thumbnail_sizes:
        try:
            generate_thumbnail(content_type.pk, instance.pk, geometry_string,
                               options)
        except:
            pass
    instance.is_processed = True
    instance.save()
    logger.info('Finished generating thumbnails for {0}'.format(instance))
