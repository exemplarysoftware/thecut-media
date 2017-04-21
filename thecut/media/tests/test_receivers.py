# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from thecut.publishing.models import Content
from django.db import models
from thecut.media import receivers


class TestAddMediaGenericRelection(TestCase):
    def test_receiver(self):
        models.signals.class_prepared.disconnect(
            receivers.add_media_generic_relation)

        class TestContent(Content):
            pass
        models.signals.class_prepared.connect(
            receivers.add_media_generic_relation)
        self.assertFalse(hasattr(TestContent, 'media'))
        receivers.add_media_generic_relation(TestContent)
        self.assertTrue(hasattr(TestContent, 'media'))
