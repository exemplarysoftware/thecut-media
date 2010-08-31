from django.contrib import admin
from media.models import Document, MediaSet


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'file',]
    search_fields = ['title']
    
    def save_model(self, request, obj, form, change):
        if not change: obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

admin.site.register(Document, DocumentAdmin)

