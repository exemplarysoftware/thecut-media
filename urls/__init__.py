from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^resources/', include('media.urls.resources')),
    (r'^galleries/', include('media.urls.galleries')),
)

