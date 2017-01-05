# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from thecut.media.admin import AttachedMediaItemMixin
from .models import MediaTestModel


@admin.register(MediaTestModel)
class MediaTestModelAdmin(AttachedMediaItemMixin, admin.ModelAdmin):

    model = MediaTestModel
