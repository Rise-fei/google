# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-06-17 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0007_auto_20200617_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchresult',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='searchresult',
            name='update_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]