# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediasources', '0002_set_ondelete'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubevideo',
            name='_oembed_data',
            field=models.TextField(default='', editable=False, blank=True),
        ),
    ]
