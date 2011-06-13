from thecut.core.forms import ModelAdminForm
from thecut.media.mediasources.models import Audio, Document, Image, Video, \
    YoutubeVideo, VimeoVideo


class AudioAdminForm(ModelAdminForm):
    class Meta:
        model = Audio


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


class VimeoVideoAdminForm(ModelAdminForm):
    def __init__(self, *args, **kwargs):
        super(VimeoVideoAdminForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False
    
    class Meta:
        model = VimeoVideo

