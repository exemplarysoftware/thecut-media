from django.forms.widgets import SelectMultiple
from django.utils.safestring import mark_safe

from django.forms.util import flatatt
from django.utils.encoding import force_unicode
from django.utils.html import escape, conditional_escape
from itertools import chain

from django.core.urlresolvers import reverse


class ImageSelectMultiple(SelectMultiple):
    help_text = 'Choose images...'
    
    class Media:
        css = {'all': ['stylesheets/image_select_multiple.css',
            'stylesheets/jquery.fancybox.css']}
        js = ['javascripts/jquery-1.4.2.js',
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
            '<a class="action initiate_image_picker" href="%s">select images</a>\
                <div class="selected_images"></div>'
            %(image_picker_url))
        return output

