# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-07-04 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acc', '0003_auto_20170704_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rzxx',
            name='rzsj',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u5165\u7ec4\u65f6\u95f4'),
        ),
    ]
