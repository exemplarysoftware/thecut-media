# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import apps
from django.db.models import signals

from . import receivers


class AppConfig(apps.AppConfig):

    name = 'thecut.media'

    def ready(self):
        signals.pre_delete.connect(
            receivers.delete_media_attachments,
            dispatch_uid='thecut.media.delete_media_attachments')
        # Let's be "helpful", and add media generic relation field to anything
        # that extends the Content model.
        signals.pre_init.connect(
            receivers.add_media_generic_relation,
            dispatch_uid='thecut.media.add_media_generic_relation')
