# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import apps


class AppConfig(apps.AppConfig):

    name = 'thecut.media'

    def __init__(self, *args, **kwargs):
        from . import receivers
        from django.db.models import signals
        signals.pre_delete.connect(receivers.delete_media_attachments)
        # Let's be helpful, and add media generic relation field to anything
        # that extends the Content model.
        signals.pre_init.connect(receivers.add_media_generic_relation)
        return super(AppConfig, self).__init__(*args, **kwargs)
