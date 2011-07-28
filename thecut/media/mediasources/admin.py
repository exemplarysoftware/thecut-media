from django.conf import settings
from django.contrib import admin
from sorl.thumbnail import get_thumbnail
from thecut.core.admin import ModelAdmin
from thecut.media.mediasources.forms import AudioAdminForm, \
    DocumentAdminForm, ImageAdminForm, VideoAdminForm, YoutubeVideoAdminForm, \
    VimeoVideoAdminForm
from thecut.media.mediasources.models import Audio, Document, Image, Video, \
    YoutubeVideo, VimeoVideo


def conditionally_register(model, adminclass):
    """Register model with admin site if it is in MEDIA_SOURCES."""
    if 'thecut.media.mediasources.models.%s' %(model.__name__) in \
        getattr(settings, 'MEDIA_SOURCES', []):
        admin.site.register(model, adminclass)


def preview_image(obj):
    html = u''
    if hasattr(obj, 'get_image'):
        try:
            thumb = get_thumbnail(obj.get_image(), '100x75', crop='center')
        except:
            pass
        else:
            html = u'<img src="%s" alt="%s" style="width:100px; ' \
                'height: 75px;" />' %(thumb.url, unicode(obj))
    return html
preview_image.short_description = 'Preview'
preview_image.allow_tags = True


class AudioAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['file', 'title', 'caption', 'content',
            'tags']}),
        ('Publishing', {'fields': [('publish_at', 'is_enabled'),
            'expire_at', 'publish_by', 'is_featured',
            ('created_at', 'created_by'),
            ('updated_at', 'updated_by')],
            'classes': ['collapse']}),
    ]
    form = AudioAdminForm
    list_display = ['title', 'publish_at', 'is_enabled', 'is_featured',
        preview_image]
    list_filter = ['publish_at', 'is_enabled', 'is_featured']
    #prepopulated_fields = {'title': ['file']}
    readonly_fields = ['created_at', 'created_by',
        'updated_at', 'updated_by']
    search_fields = ['title']

conditionally_register(Audio, AudioAdmin)


class DocumentAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['file', 'title', 'caption', 'content',
            'tags']}),
        ('Publishing', {'fields': [('publish_at', 'is_enabled'),
            'expire_at', 'publish_by', 'is_featured',
            ('created_at', 'created_by'),
            ('updated_at', 'updated_by')],
            'classes': ['collapse']}),
    ]
    form = DocumentAdminForm
    list_display = ['title', 'publish_at', 'is_enabled', 'is_featured',
        preview_image]
    list_filter = ['publish_at', 'is_enabled', 'is_featured']
    #prepopulated_fields = {'title': ['file']}
    readonly_fields = ['created_at', 'created_by',
        'updated_at', 'updated_by']
    search_fields = ['title']

conditionally_register(Document, DocumentAdmin)


class ImageAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['file', 'title', 'caption', 'content',
            'tags']}),
        ('Publishing', {'fields': [('publish_at', 'is_enabled'),
            'expire_at', 'publish_by', 'is_featured',
            ('created_at', 'created_by'),
            ('updated_at', 'updated_by')],
            'classes': ['collapse']}),
    ]
    form = ImageAdminForm
    list_display = ['title', 'publish_at', 'is_enabled', 'is_featured',
        preview_image]
    list_filter = ['publish_at', 'is_enabled', 'is_featured']
    #prepopulated_fields = {'title': ['file']}
    readonly_fields = ['created_at', 'created_by',
        'updated_at', 'updated_by']
    search_fields = ['title']

conditionally_register(Image, ImageAdmin)


class VideoAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['file', 'title', 'caption', 'content',
            'tags']}),
        ('Publishing', {'fields': [('publish_at', 'is_enabled'),
            'expire_at', 'publish_by', 'is_featured',
            ('created_at', 'created_by'),
            ('updated_at', 'updated_by')],
            'classes': ['collapse']}),
    ]
    form = VideoAdminForm
    list_display = ['title', 'publish_at', 'is_enabled', 'is_featured',
        preview_image]
    list_filter = ['publish_at', 'is_enabled', 'is_featured']
    #prepopulated_fields = {'title': ['file']}
    readonly_fields = ['created_at', 'created_by',
        'updated_at', 'updated_by']
    search_fields = ['title']

conditionally_register(Video, VideoAdmin)


class YoutubeVideoAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['url', 'title', 'caption', 'content',
            'tags']}),
        ('Publishing', {'fields': [('publish_at', 'is_enabled'),
            'expire_at', 'publish_by', 'is_featured',
            ('created_at', 'created_by'),
            ('updated_at', 'updated_by')],
            'classes': ['collapse']}),
    ]
    form = YoutubeVideoAdminForm
    list_display = ['title', 'publish_at', 'is_enabled', 'is_featured',
        preview_image]
    list_filter = ['publish_at', 'is_enabled', 'is_featured']
    #prepopulated_fields = {'title': ['file']}
    readonly_fields = ['created_at', 'created_by',
        'updated_at', 'updated_by']
    search_fields = ['title']

conditionally_register(YoutubeVideo, YoutubeVideoAdmin)


class VimeoVideoAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['url', 'title', 'caption', 'content',
            'tags']}),
        ('Publishing', {'fields': [('publish_at', 'is_enabled'),
            'expire_at', 'publish_by', 'is_featured',
            ('created_at', 'created_by'),
            ('updated_at', 'updated_by')],
            'classes': ['collapse']}),
    ]
    form = VimeoVideoAdminForm
    list_display = ['title', 'publish_at', 'is_enabled', 'is_featured',
        preview_image]
    list_filter = ['publish_at', 'is_enabled', 'is_featured']
    #prepopulated_fields = {'title': ['file']}
    readonly_fields = ['created_at', 'created_by',
        'updated_at', 'updated_by']
    search_fields = ['title']

conditionally_register(VimeoVideo, VimeoVideoAdmin)

