# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms
from tagging.forms import TagField
from thecut.core.forms import ModelAdminForm
from thecut.media.widgets import MultipleFileInput
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


class MediaUploadForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'vTextField'}))
    files = forms.FileField(widget=MultipleFileInput())
    tags = TagField(required=False, help_text=u'Separate tags with spaces, ' \
        'put quotes around multiple-word tags.', widget=forms.TextInput(
        attrs={'class': 'vTextField'}))

