from django.conf import settings
from django.conf.urls.defaults import *


urlpatterns = patterns('media.views',
    url(r'^image-picker$', 'image_picker', name='media_image_picker'),
)

if getattr(settings, 'DEBUG', False):
    urlpatterns += patterns('media.views',
        url(r'^image-picker-test$', 'image_picker_test', name='image_picker_test'),
    )

