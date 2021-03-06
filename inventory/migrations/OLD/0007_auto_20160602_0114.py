# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20160602_0101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockstatus',
            old_name='name',
            new_name='stock_stage',
        ),
        migrations.RemoveField(
            model_name='stockstatus',
            name='description',
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='mfg_name',
            field=models.CharField(blank=True, max_length=300, verbose_name='Manufacturer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_name',
            field=models.CharField(max_length=300, verbose_name='Item'),
        ),
    ]
