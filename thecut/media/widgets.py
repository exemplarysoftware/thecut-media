# -*- coding: utf-8 -*-
from django.forms.widgets import FileInput


class MultipleFileInput(FileInput):
    def render(self, name, value, attrs=None):
        attrs = attrs or {}
        attrs.update({'multiple': 'multiple'})
        return super(MultipleFileInput, self).render(name, None, attrs=attrs)

