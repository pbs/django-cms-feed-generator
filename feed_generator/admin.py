from django.db import models
from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from cms.models import Page

from feed_generator.fields import ImageField
from feed_generator.models import PageRSSFeed
from feed_generator.widgets import ImageWidget, InputWidget


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
RegisteredPageAdmin = _get_registered_modeladmin(Page)
RegisteredPageAdmin.inlines.append(RSSAdminInline)

try:
    admin.site.unregister(Page)
except NotRegistered:
    pass
admin.site.register(Page, RegisteredPageAdmin)
