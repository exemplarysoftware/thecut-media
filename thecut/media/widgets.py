# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.forms.widgets import FileInput


class MultipleFileInput(FileInput):
    def render(self, name, value, attrs=None):
        attrs = attrs or {}
        attrs.update({'multiple': 'multiple'})
        return super(MultipleFileInput, self).render(name, None, attrs=attrs)

