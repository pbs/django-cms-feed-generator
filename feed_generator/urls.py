from django.conf.urls.defaults import *
from feed_generator.feeds import RSSFeed

urlpatterns = patterns('',
    (r'^rss/$', RSSFeed()),
)
urlpatterns += patterns('feed_generator.views',
    (r'^get_file/', 'get_file'),
)