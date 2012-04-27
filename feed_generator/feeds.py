from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from cms.models.pagemodel import Page
from django.utils.feedgenerator import Rss201rev2Feed

class CustomRss201rev2Feed(Rss201rev2Feed):
    mime_type = 'text/xml; charset=utf-8'

class RSSFeed(Feed):
    feed_type = CustomRss201rev2Feed
    link = "/"

    def title(self):
        return Site.objects.get_current().name

    def description(self):
        site = Site.objects.get_current()
        return "Updates on %s" % site.domain

    def items(self):
        site = Site.objects.get_current()
        # TODO: configurable limit
        # TODO: has tag ?
        pages = Page.objects.published(site=site).order_by('-publication_date')[:30]
        return pages

    def item_title(self, item):
        # SEO page title or basic title
        return item.get_page_title() or item.get_title() 

    def item_description(self, item):
        return item.get_meta_description()

    def item_link(self, item):
        return item.get_absolute_url()

    def item_pubdate(self, item):
        return item.publication_date

