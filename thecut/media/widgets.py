from django.forms import FileInput
from django.forms.widgets import SelectMultiple
from django.forms.util import flatatt
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.utils.html import escape, conditional_escape
from itertools import chain

from django.core.urlresolvers import reverse


class DocumentSelectMultiple(SelectMultiple):
    class Media:
        css = {'all': ['media/document_select_multiple.css',
            'stylesheets/jquery.fancybox.css']}
        js = ['javascripts/jquery.js',
            'javascripts/jquery.fancybox.js',
            'media/document_select_multiple.js', 'media/csrf.js']
    
    def __init__(self, *args, **kwargs):
        super(DocumentSelectMultiple, self).__init__(*args, **kwargs)
        attrs = kwargs.pop('attrs', {})
        css_classes = attrs.get('class', '').split(' ')
        css_classes += ['document_select_multiple']
        self.attrs.update({'class': ' '.join(css_classes)})
    
    def render(self, *args, **kwargs):
        output = super(DocumentSelectMultiple, self).render(*args, **kwargs)
        document_picker_url = reverse('media_document_picker', args={})
        document_upload_url = reverse('media_document_upload', args={})
        output += mark_safe(
            '<a class="action initiate_document_upload" href="%s">Upload Document</a>\
                <a class="action initiate_document_picker" href="%s">Select Documents</a>\
                <div class="selected_documents"></div>'
            %(document_upload_url, document_picker_url))
        return output


class GallerySelectMultiple(SelectMultiple):
    class Media:
        css = {'all': ['media/gallery_select_multiple.css',
            'stylesheets/jquery.fancybox.css']}
        js = ['javascripts/jquery.js',
            'javascripts/jquery.fancybox.js',
            'media/gallery_select_multiple.js', 'media/csrf.js']
    
    def __init__(self, *args, **kwargs):
        super(GallerySelectMultiple, self).__init__(*args, **kwargs)
        attrs = kwargs.pop('attrs', {})
        css_classes = attrs.get('class', '').split(' ')
        css_classes += ['gallery_select_multiple']
        self.attrs.update({'class': ' '.join(css_classes)})
    
    def render(self, *args, **kwargs):
        output = super(GallerySelectMultiple, self).render(*args, **kwargs)
        gallery_picker_url = reverse('media_gallery_picker', args={})
        output += mark_safe(
            '<a class="action initiate_gallery_picker" href="%s">Select Galleries</a>\
                <div class="selected_galleries"></div>'
            %(gallery_picker_url))
        return output


class ImageSelectMultiple(SelectMultiple):
    class Media:
        css = {'all': ['media/image_select_multiple.css',
            'stylesheets/jquery.fancybox.css']}
        js = ['javascripts/jquery.js', 'javascripts/jquery-ui.js',
            'javascripts/jquery.form.js', 'javascripts/jquery.fancybox.js',
            'media/image_select_multiple.js', 'media/csrf.js']
    
    def __init__(self, *args, **kwargs):
        super(ImageSelectMultiple, self).__init__(*args, **kwargs)
        attrs = kwargs.pop('attrs', {})
        css_classes = attrs.get('class', '').split(' ')
        css_classes += ['image_select_multiple']
        self.attrs.update({'class': ' '.join(css_classes)})
    
    def render(self, *args, **kwargs):
        output = super(ImageSelectMultiple, self).render(*args, **kwargs)
        image_picker_url = reverse('media_image_picker', args={})
        image_upload_url = reverse('media_image_upload', args={})
        output += mark_safe(
            '<a class="action initiate_image_upload" href="%s">Upload Image</a>\
            <a class="action initiate_image_picker" href="%s">Select Images</a>\
                <div class="selected_images"></div>'
            %(image_upload_url, image_picker_url))
        return output


class ImageInput(FileInput):
    """A FileInput Widget that shows a thumbnail."""
    def render(self, *args, **kwargs):
        output = super(AdminImageWidget, self).render(*args, **kwargs)
        #if value and hasattr(value, "get_admin_thumbnail_url"):
        value = args[1]
        output = '<img src="%s" />' %(value.url) + output
        return mark_safe(output)

