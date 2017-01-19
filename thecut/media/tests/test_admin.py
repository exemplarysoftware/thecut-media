# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from thecut.media.admin import AttachedMediaItemMixin
from django.test import TestCase
from test_app.models import MediaTestModel
from test_app.admin import MediaTestModelAdmin
from django.contrib.admin.sites import AdminSite
try:  # Python 3
    from unittest import mock
except ImportError:  # Python 2
    import mock


class TestAttachedMediaItemMixin(TestCase):
    def test_get_urls(self):
        pass
        #mixin = AttachedMediaItemMixin()
        #urlpatterns = mixin.get_urls()
        #self.assertEqual(len(urlpatterns), 0)

    @mock.patch.object(MediaTestModelAdmin, 'changeform_view')
    def test_change_view(self, mock_changeform_view):
        pass
        #site = AdminSite()
        #admin = MediaTestModelAdmin(MediaTestModel, site)
        #admin.change_view(1, 2)
        #
        #self.assertEqual(mock_changeform_view.call_count, 1)
        #django_18_ok = mock_changeform_view.call_args == mock.call(1, 2, '',
        #    {'data_api_href':'../media/api/contenttypes/'})
        #django_19_ok = mock_changeform_view.call_args == mock.call(1, 2, '',
        #    {'data_api_href':'../../media/api/contenttypes/'})
        #self.assertTrue(django_18_ok or django_19_ok)

