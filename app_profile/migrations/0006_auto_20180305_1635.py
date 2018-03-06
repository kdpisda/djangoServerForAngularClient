# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-05 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0005_auto_20180305_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_type',
            field=models.CharField(choices=[('STU', 'Student'), ('HOD', 'HOD'), ('AST', 'Assistant Professor'), ('TMP', 'Temporary Faculty'), ('STF', 'Staff'), ('ALU', 'Alumni')], default='STU', max_length=3),
        ),
    ]
