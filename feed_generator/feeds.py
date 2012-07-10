import re

from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from cms.models.pagemodel import Page
from feed_generator.models import PageRSSFeed
from settings import exclude_keyword, feed_limit


def _page_in_rss(page):
    try:
        return not PageRSSFeed.objects.get(page=page).not_visible_in_feed
    except PageRSSFeed.DoesNotExist:
        pass
    return True

    

class CustomFeedGenerator(Rss201rev2Feed):
    """ Custom feed generator. Created to add extra information to the rss feed page"""
    
    def rss_attributes(self):
        """ Overriden this method to add media namespace(needed because we added media tags) """
        return {u"version": self._version,
                u"xmlns:media": u"http://search.yahoo.com/mrss/",
                "xmlns:atom": u"http://www.w3.org/2005/Atom"
                }

    def add_item_elements(self, handler, item):
        super(CustomFeedGenerator, self).add_item_elements(handler, item)
        handler.addQuickElement(u"media:description", item['short_description'])
        handler.addQuickElement(u"tags", item['tags'])
        handler.addQuickElement(u"media:thumbnail", attrs={'url':item['image_url']})

class RSSFeed(Feed):
    link = "/"
    feed_type = CustomFeedGenerator
   
    def title(self):
        return Site.objects.get_current().name

    def description(self):
        return "%s updates" % Site.objects.get_current().domain

    def items(self):
        site = Site.objects.get_current()
        feed_pages = Page.objects.published(site=site).order_by('-publication_date')
        return [feed_page for feed_page in feed_pages if _page_in_rss(feed_page)][:feed_limit]

    def item_title(self, item):
        # SEO page title or basic title
        title = item.get_page_title() or item.get_title()
        return title[:60] if title else ''

    def item_description(self, item):
        # SEO page description
        return item.get_meta_description()[:400] if item.get_meta_description() else ''

    def item_link(self, item):
        #Page url
        return item.get_absolute_url()

    def item_pubdate(self, item):
        #Page publication date
        return item.publication_date
    
    def item_extra_kwargs(self, obj):
        """
        Returns an extra keyword arguments dictionary that is used with
        the `add_item` call of the feed generator.
        Add the 'tags' field of the Page, to be used by the custom feed generator.
        """
        result = {'tags':obj.get_meta_keywords(),
                  'short_description':obj.get_meta_description()[:90] if obj.get_meta_description() else '',
                  'image_url':''}
        try:
            page_rss_feed = PageRSSFeed.objects.get(page=obj)
            result['short_description']= page_rss_feed.short_description[:90]
            result['image_url']= page_rss_feed.image_url
        except PageRSSFeed.DoesNotExist:
            pass
        return result

