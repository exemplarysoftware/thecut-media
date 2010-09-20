from django.contrib import admin
from django.contrib.contenttypes.generic import GenericStackedInline
from media.forms import MediaSetForm
from media.models import Document, MediaSet


class MediaSetInline(GenericStackedInline):
    extra = 1
    filter_horizontal = ['galleries', 'documents']
    form = MediaSetForm
    max_num = 1
    model = MediaSet


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'file',]
    search_fields = ['title']
    
    def save_model(self, request, obj, form, change):
        if not change: obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

admin.site.register(Document, DocumentAdmin)

