# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttachedMediaItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('object_id', models.IntegerField(db_index=True)),
                ('parent_object_id', models.IntegerField(db_index=True)),
                ('parent_content_type', models.ForeignKey(related_name='attachedmediaitem_parent_set', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MediaContentType',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('contenttypes.contenttype',),
        ),
        migrations.AddField(
            model_name='attachedmediaitem',
            name='content_type',
            field=models.ForeignKey(to='media.MediaContentType', on_delete=django.db.models.deletion.CASCADE),
            preserve_default=True,
        ),
    ]
