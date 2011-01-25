from django.conf.urls.defaults import *


urlpatterns = patterns('thecut.media.views',
    url(r'^$', 'gallery_list', name='gallery_list'),
    url(r'^(?P<page>\d+)$', 'gallery_list', name='paginated_gallery_list'),
    url(r'^(?P<slug>[\w-]+)$', 'gallery_detail', name='gallery_detail'),
)

