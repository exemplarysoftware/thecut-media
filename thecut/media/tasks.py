# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery.task import task
from sorl.thumbnail import get_thumbnail


@task(ignore_result=True)
def generate_thumbnail(file_, geometry_string, options):
    logger = generate_thumbnail.get_logger()
    options.update({'no_placeholder': True})
    thumbnail = get_thumbnail(file_, geometry_string, **options)
    logger.info('Generated {0} thumbnail for {1}'.format(geometry_string,
                                                         file_))
