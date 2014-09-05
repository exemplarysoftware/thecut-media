# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from ..utils import get_preview_thumbnail
from django.forms.widgets import ClearableFileInput
from django.utils.safestring import mark_safe


class AdminImageWidget(ClearableFileInput):
    """An ImageField Widget for django.contrib.admin that shows a thumbnailed
    image preview."""

    template_with_initial = '%(input_text)s: %(input)s'

    def render(self, name, value, attrs=None):
        output = super(AdminImageWidget, self).render(name, value, attrs)

        if value and hasattr(value, 'url'):
            try:
                thumbnail = get_preview_thumbnail(value)
            except Exception:
                pass
            else:
                output = '<a style="display:block;" class="image-preview" ' \
                         'href="{href}"><img src="{thumbnail.url}"></a>' \
                         '{super}'.format(href=value.url, thumbnail=thumbnail,
                                          super=output)

        return mark_safe(output)
