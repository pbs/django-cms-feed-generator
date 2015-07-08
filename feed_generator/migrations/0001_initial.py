# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import feed_generator.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageRSSFeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_description', models.CharField(max_length=255, null=True, blank=True)),
                ('image_url', feed_generator.fields.ImageField(max_length=2000, null=True, blank=True)),
                ('not_visible_in_feed', models.BooleanField(default=False, verbose_name=b'Exclude from RSS feed')),
                ('page', models.OneToOneField(to='cms.Page')),
            ],
            options={
                'verbose_name': 'RSS',
                'verbose_name_plural': 'RSS',
            },
            bases=(models.Model,),
        ),
    ]
