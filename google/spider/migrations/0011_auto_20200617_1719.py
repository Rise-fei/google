# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-06-17 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0010_auto_20200617_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchresult',
            name='td_html',
            field=models.CharField(max_length=5120, null=True),
        ),
    ]