# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-13 02:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20170813_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subprojectoverview',
            old_name='project',
            new_name='agreement',
        ),
    ]
