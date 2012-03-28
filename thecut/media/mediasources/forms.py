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
        attrs={'class': 'vTextField', 'required': 'required'}))
    files = forms.FileField(widget=MultipleFileInput(
        attrs={'required': 'required'}))
    tags = TagField(required=False, help_text='Separate tags with spaces, ' \
        'put quotes around multiple-word tags.', widget=forms.TextInput(
        attrs={'class': 'vTextField'}))
    
    class Media(forms.Media):
        css = {'all': ['media/mediasources-mediauploadform.css']}
        js = ['media/jquery.js', 'media/jquery.init.js',
            'media/mediasources-mediauploadform.js']

