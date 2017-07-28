# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from thecut.media.models import AttachedMediaItem


class AttachedMediaItemInlineForm(forms.ModelForm):

    class Media(object):
        css = {'all': ['media/attachedmediaitem_inline.css']}

    class Meta(object):
        fields = ['order', 'content_type', 'object_id']
        model = AttachedMediaItem
