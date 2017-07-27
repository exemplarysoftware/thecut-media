# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediasources', '0003_youtubevideo__oembed_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vimeovideo',
            name='url',
            field=models.URLField(help_text='e.g. https://vimeo.com/123456'),
        ),
    ]
