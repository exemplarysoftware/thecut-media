# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediasources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='created_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='audio',
            name='publish_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='audio',
            name='updated_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='document',
            name='created_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='document',
            name='publish_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='updated_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='created_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='publish_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='updated_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='video',
            name='created_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='video',
            name='publish_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='updated_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vimeovideo',
            name='created_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vimeovideo',
            name='publish_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='vimeovideo',
            name='updated_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='youtubevideo',
            name='created_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='youtubevideo',
            name='publish_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='youtubevideo',
            name='updated_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, editable=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
