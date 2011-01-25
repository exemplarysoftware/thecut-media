from django.conf import settings
from django.conf.urls.defaults import *


urlpatterns = patterns('thecut.media.views',
    url(r'^image-picker$', 'image_picker', name='media_image_picker'),
    url(r'^gallery-picker$', 'gallery_picker', name='media_gallery_picker'),
    url(r'^document-picker$', 'document_picker', name='media_document_picker'),
)

if getattr(settings, 'DEBUG', False):
    urlpatterns += patterns('thecut.media.views',
        url(r'^image-picker-test$', 'image_picker_test', name='image_picker_test'),
    )

