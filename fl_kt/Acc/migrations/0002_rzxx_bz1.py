# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-07-04 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rzxx',
            name='bz1',
            field=models.TextField(max_length=500, null=True, verbose_name='\u5907\u6ce81'),
        ),
    ]