# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 06:48
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_set_ondelete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachedmediaitem',
            name='parent_object_id',
            field=models.TextField(db_index=True),
        ),
    ]
