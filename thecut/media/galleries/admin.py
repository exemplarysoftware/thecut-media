from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline
from sorl.thumbnail import get_thumbnail
from thecut.core.admin import ModelAdmin
from thecut.media.galleries.forms import GalleryAdminForm
from thecut.media.galleries.models import Gallery


GALLERY_INLINES = []

if 'thecut.media' in settings.INSTALLED_APPS:
    try:
        from thecut.media.admin import MediaSetInline
    except ImportError:
        pass
    else:
        GALLERY_INLINES += [MediaSetInline]


if 'ctas' in settings.INSTALLED_APPS:
    try:
        from ctas.models import AttachedCallToAction
    except ImportError:
        pass
    else:
        class GalleryCallToActionInline(GenericTabularInline):
            extra = 1
            max_num = 1
            model = AttachedCallToAction
            exclude = ['order']
        
        GALLERY_INLINES += [GalleryCallToActionInline]


def preview_image(obj):
    if hasattr(obj.media, 'get_image'):
        thumb = get_thumbnail(obj.media.get_image(), '100x75',
            crop='center')
        return u'<img src="%s" alt="%s" />' %(thumb.url, str(obj))
    else:
        return u''
preview_image.short_description = 'Preview'
preview_image.allow_tags = True


class GalleryAdmin(ModelAdmin):
    date_hierarchy = 'publish_at'
    fieldsets = [
        (None, {'fields': ['title', 'headline', 'content',
            'meta_description', 'tags']}),
        ('Publishing', {'fields': ['sites', 'slug',
            ('publish_at', 'is_enabled'), 'expire_at', 'publish_by',
            'template', 'is_featured', 'is_indexable',
            ('created_at', 'created_by'),
            ('updated_at', 'updated_by')],
            'classes': ['collapse']}),
    ]
    form = GalleryAdminForm
    inlines = GALLERY_INLINES
    list_display = ['title', 'publish_at', 'is_enabled',
        'is_featured', 'is_indexable', preview_image]
    list_filter = ['publish_at', 'is_enabled', 'is_featured',
        'is_indexable']
    prepopulated_fields = {'slug': ['title']}
    readonly_fields = ['created_at', 'created_by',
        'updated_at', 'updated_by']
    search_fields = ['title']

admin.site.register(Gallery, GalleryAdmin)

