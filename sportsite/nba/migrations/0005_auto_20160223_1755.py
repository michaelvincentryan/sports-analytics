# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 17:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nba', '0004_auto_20160223_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='standings',
            old_name='year',
            new_name='date',
        ),
    ]
