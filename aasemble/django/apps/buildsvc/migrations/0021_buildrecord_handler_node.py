# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import socket


class Migration(migrations.Migration):

    dependencies = [
        ('buildsvc', '0020_auto_20160127_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildrecord',
            name='handler_node',
            field=models.CharField(default=socket.getfqdn, max_length=100, null=True),
        ),
    ]
