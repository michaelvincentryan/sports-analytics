# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 19:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nba', '0007_auto_20160223_1957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conference',
            old_name='conference',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='division',
            old_name='division',
            new_name='name',
        ),
    ]
