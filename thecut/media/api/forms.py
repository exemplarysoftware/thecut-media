# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms


class FilterForm(forms.Form):

    q = forms.CharField(required=False)

    def clean_q(self):
        return [t.strip() for t in self.cleaned_data['q'].split() if t]

    def filter_queryset(self, queryset):
        for term in self.cleaned_data.get('q', []):
            queryset = queryset.filter(title__icontains=term)
        return queryset
