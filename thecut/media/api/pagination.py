# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from taggit.models import Tag


class DefaultPagination(PageNumberPagination):

    page_query_param = 'page'

    page_size = 10

    page_size_query_param = 'limit'

    max_page_size = 100


class TaggedPagination(DefaultPagination):

    def paginate_queryset(self, queryset, request, view, *args, **kwargs):
        self.view = view
        return super(TaggedPagination, self).paginate_queryset(
            queryset, request, view, *args, **kwargs)

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data),
            ('tags', self.get_tags(data))
        ]))

    def get_tags(self, data):
        tag_pks = self.view.get_queryset().values_list(
            'tags', flat=True).distinct()
        tag_queryset = Tag.objects.filter(pk__in=tag_pks)
        return tag_queryset.values_list('name', flat=True)
