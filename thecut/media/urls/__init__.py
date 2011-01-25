from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^resources/', include('thecut.media.urls.resources')),
    (r'^galleries/', include('thecut.media.urls.galleries')),
)

