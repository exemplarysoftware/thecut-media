# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os

DEBUG = True

USE_TZ = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'thecut.exampleapp',
    'test_app',
]

SITE_ID = 1

SECRET_KEY = 'thecut'

MIDDLEWARE_CLASSES = []  # silences dj1.7 warning

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'loaders': [
                ('django.template.loaders.cached.Loader',
                 ['django.template.loaders.filesystem.Loader',
                  'django.template.loaders.app_directories.Loader'])
            ],
        },
    },
],

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..')
