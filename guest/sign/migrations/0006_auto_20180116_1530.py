# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-16 15:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0005_auto_20180116_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='limit',
            new_name='people_limit',
        ),
    ]
