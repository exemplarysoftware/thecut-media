from django.test import TestCase
from thecut.media.utils import get_media_source_models
from thecut.media.mediasources.models import (Audio, Document, Image, Video,
                                              VimeoVideo, YoutubeVideo)

class TestGetMediaSourceModels(TestCase):
    def test_get_media_source_models(self):
        models = set(get_media_source_models())
        self.assertEqual(models, {Audio, Document, Image, Video, VimeoVideo,
                                  YoutubeVideo})

