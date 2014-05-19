# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


DOCUMENT = [
    'application/pdf',
    'application/postscript',
    'application/vnd.ms-xpsdocument',
]

WORD_PROCESSING = [
    'application/vnd.oasis.opendocument.text',
    'application/msword',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    ]

SPREADSHEET = [
    'application/vnd.oasis.opendocument.spreadsheet',
    'application/vnd.ms-excel',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    ]

PRESENTATION = [
    'application/vnd.oasis.opendocument.presentation',
    'application/vnd.ms-powerpoint',
    'application/vnd.openxmlformats-officedocument.presentationml.presentation'
    ]

ALL_DOCUMENTS = DOCUMENT + WORD_PROCESSING + SPREADSHEET + PRESENTATION


IMAGE = [
    'image/gif',
    'image/jpeg',
    'image/png',
    'image/svg+xml',
    'image/tiff'
    ]


VIDEO = [
    'video/avi',
    'video/mpeg',
    'video/mp4',
    'video/ogg',
    'video/quicktime',
    'video/webm',
    'video/x-matroska',
    'video/x-ms-wmv',
    'video/x-flv',
    ]


AUDIO = [
    'audio/aac',
    'audio/aacp',
    'audio/L24',
    'audio/mp4',
    'audio/mpeg',
    'audio/ogg',
    'audio/opus',
    'audio/vorbis'
    'audio/vnd.wave',
    'audio/webm',
    'audio/x-ms-wma',
    ]
