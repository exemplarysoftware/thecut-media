# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from thecut.core.forms import ModelAdminForm
from thecut.media.galleries.models import Gallery


class GalleryAdminForm(ModelAdminForm):
    class Meta:
        model = Gallery

