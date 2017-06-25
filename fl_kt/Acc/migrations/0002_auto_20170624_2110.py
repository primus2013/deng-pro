# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-24 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Acc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rzxx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sbcj', models.CharField(max_length=50, verbose_name='\u8bbe\u5907\u5382\u5bb6')),
                ('sbxh', models.CharField(max_length=50, verbose_name='\u8bbe\u5907\u578b\u53f7')),
                ('rzsj', models.DateTimeField(auto_now_add=True, verbose_name='\u5165\u7ec4\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u533b\u9662\u540d\u79f0',
                'verbose_name_plural': '\u533b\u9662\u540d\u79f0',
            },
        ),
        migrations.CreateModel(
            name='Sbcj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cjmc', models.CharField(max_length=50, verbose_name='\u5382\u5bb6\u540d\u79f0')),
                ('szdq', models.CharField(max_length=50, verbose_name='\u6240\u5728\u5730\u533a')),
            ],
            options={
                'verbose_name': '\u5382\u5bb6\u540d\u79f0',
                'verbose_name_plural': '\u5382\u5bb6\u540d\u79f0',
            },
        ),
        migrations.CreateModel(
            name='Sbxh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sbxh', models.CharField(max_length=50, verbose_name='\u8bbe\u5907\u578b\u53f7')),
                ('leix', models.CharField(max_length=50, verbose_name='\u8bbe\u5907\u7c7b\u578b')),
            ],
            options={
                'verbose_name': '\u8bbe\u5907\u578b\u53f7',
                'verbose_name_plural': '\u8bbe\u5907\u578b\u53f7',
            },
        ),
        migrations.CreateModel(
            name='Yyxx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yymc', models.CharField(max_length=50, verbose_name='\u533b\u9662\u540d\u79f0')),
                ('shengf', models.CharField(max_length=50, verbose_name='\u6240\u5728\u7701\u4efd')),
                ('dengj', models.CharField(max_length=50, verbose_name='\u533b\u9662\u7b49\u7ea7')),
            ],
            options={
                'verbose_name': '\u533b\u9662\u540d\u79f0',
                'verbose_name_plural': '\u533b\u9662\u540d\u79f0',
            },
        ),
        migrations.AddField(
            model_name='rzxx',
            name='yymc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Acc.Yyxx', verbose_name='\u533b\u9662\u540d\u79f0'),
        ),
    ]
