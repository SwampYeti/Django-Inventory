# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 23:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20160601_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manufacturer',
            name='mfg_url',
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='password',
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='username',
        ),
    ]
