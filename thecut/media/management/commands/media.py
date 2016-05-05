# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option


class Command(BaseCommand):

    args = '[findthumbnails] [queuethumbnails]'

    option_list = BaseCommand.option_list + (
        make_option('--quantity', action='store', type='int', dest='quantity',
                    default=1, help='Number of instances to create'),
        )

    help = ('findthumbnails: Attempt to find thumbnail references in '
            'templates\n'
            'queuethumbnails: Queue thumbnail generation for media instances.')

    def _find_thumbnails(self):
        from thecut.media.utils import find_thumbnails_in_templates
        output = find_thumbnails_in_templates()
        try:
            self.stdout.write(output)
        except AttributeError:
            print(output)

    def _queue_thumbnails(self):
        from thecut.media.utils import queue_thumbnails
        output = queue_thumbnails()
        try:
            self.stdout.write(output)
        except AttributeError:
            print(output)

    def handle(self, command, *args, **options):

        if command not in ['findthumbnails', 'queuethumbnails']:
            raise CommandError('"{0}" is not a valid argument'.format(command))

        if command == 'findthumbnails':
            return self._find_thumbnails()

        if command == 'queuethumbnails':
            return self._queue_thumbnails()
