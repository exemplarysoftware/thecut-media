from django.contrib import admin
from django.contrib.contenttypes.generic import GenericStackedInline
from thecut.media.models import MediaSet


class MediaSetInline(GenericStackedInline):
    extra = 1
    #form = MediaSetForm
    max_num = 1
    model = MediaSet

