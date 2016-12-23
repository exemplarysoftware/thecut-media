# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from thecut.media.admin import AttachedMediaItemMixin
from django.test import TestCase


class TestAttachedMediaItemMixin(TestCase):
    def test_get_urls(self):
        pass
        #mixin = AttachedMediaItemMixin()
        #urlpatterns = mixin.get_urls()
        #self.assertEqual(len(urlpatterns), 0)
