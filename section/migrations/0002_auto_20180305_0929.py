# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-05 09:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Achievements',
            new_name='Achievement',
        ),
    ]
