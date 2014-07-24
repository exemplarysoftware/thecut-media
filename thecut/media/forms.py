# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms
from django.contrib.contenttypes.models import ContentType
from thecut.media import MEDIA_SOURCE_CLASSES
from thecut.media.models import AttachedMediaItem


class AttachedMediaItemInlineForm(forms.ModelForm):

    class Media(object):
        css = {'all': ['media/attachedmediaitem_inline.css']}
        js = ['media/lib/require.js', 'media/attachedmediaitem_inline.js']

    class Meta(object):
        # TODO: fields = []
        model = AttachedMediaItem


class MediaSearchForm(forms.Form):

    q = forms.CharField(required=False)
    tags = forms.MultipleChoiceField(required=False, choices=[],
                                     widget=forms.CheckboxSelectMultiple())

    def __init__(self, tag_list, *args, **kwargs):
        super(MediaSearchForm, self).__init__(*args, **kwargs)
        self.fields['tags'].choices = [(t.pk, t.name) for t in tag_list]
