# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions


__all__ = ['IssuePermissions', 'IsAdminUser']


class IssuePermissions(DjangoModelPermissions):
    """Extended version of DjangoModelPermissions which checks for ``change``
    permissions for GET, OPTIONS, and HEAD requests."""
    perms_map = {
        'GET': ['moderation.change_issue'],
        'OPTIONS': ['moderation.change_issue'],
        'HEAD': ['moderation.change_issue'],
        'POST': ['moderation.add_issue'],
        'PUT': ['moderation.change_issue'],
        'PATCH': ['moderation.change_issue'],
        'DELETE': ['moderation.delete_issue'],
    }
