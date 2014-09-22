# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from ..utils import get_content_type
from ..widgets import AdminImageWidget
from django import forms
from taggit.forms import TagField
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
        widgets = {'file': AdminImageWidget}


class VideoAdminForm(OrderMixin, forms.ModelForm):

    class Meta(object):
        model = Video
        widgets = {'file': AdminImageWidget}


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

    files = forms.FileField()

    title = forms.CharField(
        required=False, max_length=200,
        widget=forms.TextInput(attrs={'class': 'vTextField'}))

    tags = TagField(required=False, help_text='Separate tags with commas, '
                    'put quotes around multiple-word tags.')

    class Media(object):
        css = {'all': ['media/mediasources-mediauploadform.css']}
        js = ['media/mediasources-mediauploadform.js']

    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop('content_types', None)
        super(MediaUploadForm, self).__init__(*args, **kwargs)

        # Set the attributes on the 'files' widget so that the
        # filepicker only shows files which are one of the defined
        # content types.
        attrs = {'required': 'required'}
        if self.content_types:
            attrs.update({'accept': ','.join(content_type for content_type
                                             in self.content_types)})
        self.fields['files'].widget = MultipleFileInput(attrs=attrs)

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
