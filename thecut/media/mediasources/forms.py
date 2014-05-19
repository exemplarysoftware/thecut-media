# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .utils import get_content_type
from django import forms
from tagging.forms import TagField
from thecut.media.widgets import MultipleFileInput
from thecut.media.mediasources.models import (Audio, Document, Image, Video,
                                              YoutubeVideo, VimeoVideo)
from thecut.ordering.forms import OrderMixin


class AudioAdminForm(OrderMixin, forms.ModelForm):

    class Meta(object):
        model = Audio


class DocumentAdminForm(OrderMixin, forms.ModelForm):

    class Meta(object):
        model = Document


class ImageAdminForm(OrderMixin, forms.ModelForm):

    class Meta(object):
        model = Image


class VideoAdminForm(OrderMixin, forms.ModelForm):

    class Meta(object):
        model = Video


class YoutubeVideoAdminForm(OrderMixin, forms.ModelForm):

    class Meta(object):
        model = YoutubeVideo


class VimeoVideoAdminForm(OrderMixin, forms.ModelForm):

    class Meta(object):
        model = VimeoVideo

    def __init__(self, *args, **kwargs):
        super(VimeoVideoAdminForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False


class MediaUploadForm(forms.Form):

    files = forms.FileField(
        widget=MultipleFileInput(attrs={'required': 'required'}))

    title = forms.CharField(
        required=False, max_length=200,
        widget=forms.TextInput(attrs={'class': 'vTextField'}))

    tags = TagField(required=False, help_text='Separate tags with spaces, '
                    'put quotes around multiple-word tags.',
                    widget=forms.TextInput(attrs={'class': 'vTextField'}))

    class Media(object):
        css = {'all': ('media/mediasources-mediauploadform.css',)}
        js = ('media/jquery.js', 'media/jquery.init.js',
              'media/mediasources-mediauploadform.js')

    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop('content_types', None)
        return super(MediaUploadForm, self).__init__(*args, **kwargs)

    def clean_files(self, *args, **kwargs):
        files = self.cleaned_data['files']
        if self.files and self.content_types is not None:
            for upload in self.files.getlist('files'):
                content_type = get_content_type(upload)
                if content_type not in self.content_types:
                    raise forms.ValidationError(
                        '"{0}" is not a supported file type.'.format(
                            content_type))
        return files
