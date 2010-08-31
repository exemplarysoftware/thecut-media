from django.forms.widgets import SelectMultiple
from django.utils.safestring import mark_safe

from django.forms.util import flatatt
from django.utils.encoding import force_unicode
from django.utils.html import escape, conditional_escape
from itertools import chain

from django.core.urlresolvers import reverse


class DocumentSelectMultiple(SelectMultiple):
    class Media:
        css = {'all': ['stylesheets/document_select_multiple.css',
            'stylesheets/jquery.fancybox.css']}
        js = ['javascripts/jquery.js',
            'javascripts/jquery.fancybox.js',
            'javascripts/document_select_multiple.js']
    
    def __init__(self, *args, **kwargs):
        super(DocumentSelectMultiple, self).__init__(*args, **kwargs)
        attrs = kwargs.pop('attrs', {})
        css_classes = attrs.get('class', '').split(' ')
        css_classes += ['document_select_multiple']
        self.attrs.update({'class': ' '.join(css_classes)})
    
    def render(self, *args, **kwargs):
        output = super(DocumentSelectMultiple, self).render(*args, **kwargs)
        document_picker_url = reverse('media_document_picker', args={})
        output += mark_safe(
            '<a class="action initiate_document_picker" href="%s">Select Documents</a>\
                <div class="selected_documents"></div>'
            %(document_picker_url))
        return output


class GallerySelectMultiple(SelectMultiple):
    class Media:
        css = {'all': ['stylesheets/gallery_select_multiple.css',
            'stylesheets/jquery.fancybox.css']}
        js = ['javascripts/jquery.js',
            'javascripts/jquery.fancybox.js',
            'javascripts/gallery_select_multiple.js']
    
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
        css = {'all': ['stylesheets/image_select_multiple.css',
            'stylesheets/jquery.fancybox.css']}
        js = ['javascripts/jquery.js',
            'javascripts/jquery.fancybox.js',
            'javascripts/image_select_multiple.js']
    
    def __init__(self, *args, **kwargs):
        super(ImageSelectMultiple, self).__init__(*args, **kwargs)
        attrs = kwargs.pop('attrs', {})
        css_classes = attrs.get('class', '').split(' ')
        css_classes += ['image_select_multiple']
        self.attrs.update({'class': ' '.join(css_classes)})
    
    def render(self, *args, **kwargs):
        output = super(ImageSelectMultiple, self).render(*args, **kwargs)
        image_picker_url = reverse('media_image_picker', args={})
        output += mark_safe(
            '<a class="action initiate_image_picker" href="%s">Select Images</a>\
                <div class="selected_images"></div>'
            %(image_picker_url))
        return output

