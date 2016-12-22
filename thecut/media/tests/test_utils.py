from django.test import TestCase
from thecut.media.utils import get_media_source_models

class TestGetMediaSourceModels(TestCase):
    def test_get_media_source_models(self):
        models = set(get_media_source_models())
        self.assertEqual(models, set())

