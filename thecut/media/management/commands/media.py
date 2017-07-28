# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from pprint import pformat

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    help = ('findthumbnails: Attempt to find thumbnail references in '
            'templates\n'
            'queuethumbnails: Queue thumbnail generation for media instances.')

    def add_arguments(self, parser):
        parser.add_argument('command')

    def _find_thumbnails(self):
        from thecut.media.utils import find_thumbnails_in_templates
        output = find_thumbnails_in_templates()
        self.stdout.write(pformat(output))

    def _queue_thumbnails(self):
        from thecut.media.utils import queue_thumbnails
        output = queue_thumbnails()
        self.stdout.write(pformat(output))

    def handle(self, *args, **options):
        command = options.get('command')

        if command not in ['findthumbnails', 'queuethumbnails']:
            raise CommandError('"{}" is not a valid argument'.format(command))

        if command == 'findthumbnails':
            return self._find_thumbnails()

        if command == 'queuethumbnails':
            return self._queue_thumbnails()
