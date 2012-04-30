django-cms-feed-generator
=========================

Simple django-cms addon that exposes a RSS feed endpoint containing the last created pages with title and description.

INSTALL

1. $ python setup.py install
2. edit project settings and add "feed_generator" to INSTALLED_APPS
3. edit project urls.py and add an entry similar to this one:
   url(r'^news/', include('feed_generator.urls')),

This will expose the RSS feet at http://site.com/news/rss

