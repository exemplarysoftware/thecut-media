# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser

__all__ = ['MediaPermissions', 'IsAdminUser']


class MediaPermissions(DjangoModelPermissions):
    """Extended version of DjangoModelPermissions which checks for ``change``
    permissions for GET, OPTIONS, and HEAD requests."""

    perms_map = {
        'GET': ['media.change_attachedmediaitem'],
        'OPTIONS': ['media.change_attachedmediaitem'],
        'HEAD': ['media.change_attachedmediaitem'],
        'POST': ['media.add_attachedmediaitem'],
        'PUT': ['media.change_attachedmediaitem'],
        'PATCH': ['media.change_attachedmediaitem'],
        'DELETE': ['media.delete_attachedmediaitem'],
    }
