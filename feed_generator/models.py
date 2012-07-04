from cms.models import Page
from django.db import models

class PageRSSFeed(models.Model):
    page = models.OneToOneField(Page)
    short_description = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'RSS'
        verbose_name_plural = 'RSS'

    def __unicode__(self):
        return self.short_description[0:50]
