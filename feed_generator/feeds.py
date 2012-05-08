import re

from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed 
from cms.models.pagemodel import Page
from pagetags.models import PageTagging
from settings import exclude_keyword, feed_limit


def _page_in_rss(page):
    if PageTagging.objects.filter(page=page).count():
        tag_list = [item.strip().lower() for item in page.pagetagging.page_tags.split(",")]
        return exclude_keyword.lower() not in tag_list
    return []
    

class CustomFeedGenerator(Rss201rev2Feed):
    """ Custom feed generatior. Created to add extra information to the rss feed page"""

    def add_item_elements(self, handler, item):
        super(CustomFeedGenerator, self).add_item_elements(handler, item)
        handler.addQuickElement(u"tags", item['tags'])


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
        return [feed_page for feed_page in feed_pages if _page_in_rss(feed_page)][:feed_limits]

    def item_title(self, item):
        # SEO page title or basic title
        return item.get_page_title() or item.get_title() 

    def item_description(self, item):
        # SEO page description
        return item.get_meta_description()

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
        return { 'tags': obj.get_meta_keywords(),}

