from thecut.core.forms import ModelAdminForm
from thecut.media.mediasources.models import Document, Image, Video, YoutubeVideo


class DocumentAdminForm(ModelAdminForm):
    class Meta:
        model = Document


class ImageAdminForm(ModelAdminForm):
    class Meta:
        model = Image


class VideoAdminForm(ModelAdminForm):
    class Meta:
        model = Video


class YoutubeVideoAdminForm(ModelAdminForm):
    class Meta:
        model = YoutubeVideo

