from django.conf.urls.defaults import *
from feed_generator.feeds import RSSFeed

urlpatterns = patterns('',
    (r'^rss/$', RSSFeed()),
)
