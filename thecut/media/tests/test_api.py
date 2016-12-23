# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from thecut.media.api.serializers import MediaFileUpload
from thecut.media.api.urls import generate_urls
from thecut.media.utils import get_media_source_models


class TestApiGenerateUrls(TestCase):
    def test_generate_urls(self):
        result = generate_urls('admin','namespace', get_media_source_models())
        # Not exactly sure what we should be testing here
        self.assertEqual(len(result), 1)

