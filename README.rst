django-cms-feed-generator
=========================

``feed-generator`` is a simple `django-cms`_ addon that exposes a RSS feed endpoint containing the last pages created in the CMS.

Instalation
===========

1. $ python setup.py install
2. edit project settings.py and add "feed_generator" to INSTALLED_APPS
3. edit project urls.py and add an entry similar to this one:
   url(r'^news/', include('feed_generator.urls')),

This will expose the RSS feed at http://yoursite.com/news/rss

Settings
========

* ``FEEDGENERATOR_FEED_LIMIT`` the maximum number of pages to include in the feed, defaults to ``100``.
* ``FEEDGENERATOR_EXCLUDE_KEYWORD`` the pages that contain this keyword will be excluded from the feed.

.. _django-cms:
    http://django-cms.org/

