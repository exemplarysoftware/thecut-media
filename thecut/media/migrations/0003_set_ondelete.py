# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20150818_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachedmediaitem',
            name='content_type',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.CASCADE, to='media.MediaContentType'),
        ),
    ]
