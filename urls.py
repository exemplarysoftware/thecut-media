from django.conf import settings
from django.conf.urls.defaults import *


urlpatterns = patterns('media.views',
    url(r'^image-picker$', 'image_picker', name='media_image_picker'),
)

if getattr(settings, 'DEBUG', False):
    urlpatterns += patterns('media.views',
        url(r'^test$', 'test', name='test'),
    )

