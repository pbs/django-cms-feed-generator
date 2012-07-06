from django.db import models
from django.contrib import admin
from models import PageRSSFeed
from cms.models import Page
from django.contrib.admin.sites import NotRegistered
from fields import ImageField
from widgets import ImageWidget, InputWidget


def _get_registered_modeladmin(model):
    """ This is a huge hack to get the registered modeladmin for the model.
        We need this functionality in case someone else already registered
        a different modeladmin for this model. """
    return type(admin.site._registry[model])


class RSSAdminInline(admin.StackedInline):
    model = PageRSSFeed
    formfield_overrides = {
        ImageField: {
            'widget': ImageWidget(attrs={'maxlength': 2000, 'size': 60})
        },
        models.CharField: {
            'widget': InputWidget(attrs={'maxlength': 255, 'size': 60})
        }
    }

# This is a huge hack to get the registered modeladmin for the model.
# We need this functionality in case someone else already registered a different modeladmin for this model. """
RegisteredPageAdmin = type(admin.site._registry[Page])

#XXX: django-cms changes the inlines dynamically based on the user rights but
# fails to properly clean everything and breaks all inlines added at the end
# of the list. Prepending the page tagging plugin fixes this.
RegisteredPageAdmin.inlines = [RSSAdminInline] + RegisteredPageAdmin.inlines

try:
    admin.site.unregister(Page)
except NotRegistered:
    pass
admin.site.register(Page, RegisteredPageAdmin)
