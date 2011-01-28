from django.conf import settings
from django.conf.urls.defaults import *


urlpatterns = patterns('thecut.media.views',
    url(r'^image-picker$', 'image_picker', name='media_image_picker'),
    url(r'^image-upload$', 'image_upload', name='media_image_upload'),
    url(r'^gallery-picker$', 'gallery_picker', name='media_gallery_picker'),
    url(r'^document-picker$', 'document_picker', name='media_document_picker'),
    url(r'^document-upload$', 'document_upload', name='media_document_upload'),
)

if getattr(settings, 'DEBUG', False):
    urlpatterns += patterns('thecut.media.views',
        url(r'^image-picker-test$', 'image_picker_test', name='image_picker_test'),
    )

