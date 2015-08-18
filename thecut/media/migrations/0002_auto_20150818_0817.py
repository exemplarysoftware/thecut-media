# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachedmediaitem',
            options={'ordering': ['order', 'pk']},
        ),
    ]
