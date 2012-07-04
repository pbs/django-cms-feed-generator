from cms.models import Page
from django.db import models

class PageRSSFeed(models.Model):
    page = models.OneToOneField(Page)

    class Meta:
        verbose_name = 'RSS'
        verbose_name_plural = 'RSS'
