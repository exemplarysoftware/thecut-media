from django.contrib import admin
from django.contrib.contenttypes.generic import GenericStackedInline
from media.forms import DocumentAdminForm, GalleryAdminForm, MediaSetForm
from media.models import Document, Gallery, MediaSet


class MediaSetInline(GenericStackedInline):
    extra = 1
    form = MediaSetForm
    max_num = 1
    model = MediaSet


class DocumentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'file']}),
        ('Publishing', {'fields': [('publish_at', 'is_enabled'),
            'publish_by', 'is_featured'], 'classes': ['collapse']}),
    ]
    form = DocumentAdminForm
    list_display = ['title', 'mime_type', 'publish_at', 'is_enabled',
        'is_featured']
    list_filter = ['publish_at', 'is_enabled', 'is_featured']
    search_fields = ['title']
    
    def save_model(self, request, obj, form, change):
        if not change: obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()
admin.site.register(Document, DocumentAdmin)


class GalleryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'headline', 'images',
            'image_order', 'content', 'meta_description', 'tags']}),
        ('Publishing', {'fields': ['sites', 'slug',
            ('publish_at', 'is_enabled'), 'publish_by', 'template',
            'is_featured', 'is_indexable'], 'classes': ['collapse']}),
    ]
    form = GalleryAdminForm
    list_display = ['title', 'publish_at', 'is_enabled',
        'is_featured', 'is_indexable']
    list_filter = ['publish_at', 'is_enabled', 'is_featured',
        'is_indexable']
    prepopulated_fields = {'slug': ['title']}
    search_fields = ['title']
    
    def save_model(self, request, obj, form, change):
        if not change: obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()
admin.site.register(Gallery, GalleryAdmin)

