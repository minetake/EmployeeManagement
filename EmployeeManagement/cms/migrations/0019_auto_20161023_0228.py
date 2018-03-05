# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0018_subprojectoverview_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subprojectoverview',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='終了日'),
        ),
        migrations.AlterField(
            model_name='subprojectoverview',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='開始日'),
        ),
    ]
