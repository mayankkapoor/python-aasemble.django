# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildsvc', '0021_buildrecord_handler_node'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildrecord',
            name='state',
            field=models.SmallIntegerField(choices=[(1, b'Building'), (2, b'Succesfully Built'), (3, b'Chroot Problem'), (4, b'Build for superseded source'), (5, b'Failed to build'), (6, b'Dependency wait'), (7, b'Failed to upload'), (8, b'Needs building'), (9, b'Unknown (predates state tracking)')], default=9),
        ),
    ]
