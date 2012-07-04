from django.contrib import admin
from models import PageRSSFeed
from cms.models import Page
from django.contrib.admin.sites import NotRegistered

def _get_registered_modeladmin(model):
    """ This is a huge hack to get the registered modeladmin for the model.
        We need this functionality in case someone else already registered
        a different modeladmin for this model. """
    return type(admin.site._registry[model])


class RSSAdminInline(admin.StackedInline):
    model = PageRSSFeed

RegisteredPageAdmin = _get_registered_modeladmin(Page)
RegisteredPageAdmin.inlines = [RSSAdminInline,] + RegisteredPageAdmin.inlines

try:
    admin.site.unregister(Page)
except NotRegistered:
    pass
admin.site.register(Page, RegisteredPageAdmin)
