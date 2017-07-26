# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import utils as receivers
from django import apps
from django.db.models import signals


class AppConfig(apps.AppConfig):

    name = 'thecut.media.mediasources'

    def ready(self):
        signals.post_save.connect(
            receivers.generate_thumbnails, sender='mediasources.Document',
            dispatch_uid='mediasources.Document.generate_thumbnails')
        signals.post_save.connect(
            receivers.generate_thumbnails, sender='mediasources.Image',
            dispatch_uid='mediasources.Image.generate_thumbnails')
        signals.post_save.connect(
            receivers.generate_thumbnails, sender='mediasources.Video',
            dispatch_uid='mediasources.Video.generate_thumbnails')
        signals.post_save.connect(
            receivers.generate_thumbnails, sender='mediasources.VimeoVideo',
            dispatch_uid='mediasources.VimeoVideo.generate_thumbnails')
        signals.post_save.connect(
            receivers.generate_thumbnails, sender='mediasources.YoutubeVideo',
            dispatch_uid='mediasources.YoutubeVideo.generate_thumbnails')

        signals.pre_delete.connect(
            receivers.delete_file, sender='mediasources.Audio',
            dispatch_uid='mediasources.Audio.delete_file')
        signals.pre_delete.connect(
            receivers.delete_file, sender='mediasources.Document',
            dispatch_uid='mediasources.Document.delete_file')
        signals.pre_delete.connect(
            receivers.delete_file, sender='mediasources.Image',
            dispatch_uid='mediasources.Image.delete_file')
        signals.pre_delete.connect(
            receivers.delete_file, sender='mediasources.Video',
            dispatch_uid='mediasources.Video.delete_file')
