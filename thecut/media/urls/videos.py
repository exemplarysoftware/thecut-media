from django.conf.urls.defaults import *


urlpatterns = patterns('thecut.media.views',
    url(r'^$', 'video_list', name='video_list'),
    url(r'^(?P<page>\d+)$', 'video_list', name='paginated_video_list'),
    url(r'^(?P<slug>[\w-]+)$', 'video_detail', name='video_detail'),
)

