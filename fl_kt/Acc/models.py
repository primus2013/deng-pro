# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser   # 此处是用户数据模型可以继承django已有的AbstractUser模型用（是一个关于用户的）


class User(AbstractUser):
    avatar=models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True,
                             null=True, verbose_name='用户头像' )
    qq=models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    mobil=models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')

    class Meta:
        verbose_name='用户列表'
        verbose_name_plural=verbose_name
        ordering=['-id']

        def __unicode__(self):
            return self.username

# 医院字典


class Yyxx(models.Model):
    yymc = models.CharField(max_length=50, verbose_name='医院名称')
    shengf = models.CharField(max_length=50, verbose_name='所在省份')
    dengj = models.CharField(max_length=50, verbose_name='医院等级')

    class Meta:
        verbose_name = '医院字典'
        verbose_name_plural = verbose_name
        ordering = ['-yymc', 'dengj']

    def __unicode__(self):
        return self.yymc


# 厂家字典
class Sbcj(models.Model):
    cjmc = models.CharField(max_length=50, null=True, verbose_name='厂家名称')
    szdq = models.CharField(max_length=50, verbose_name='所在地区')

    class Meta:
        verbose_name = '厂家字典'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.cjmc

# 设备字典
class Sbxh(models.Model):
    sbxh = models.CharField(max_length=50, verbose_name='设备型号')
    leix = models.CharField(max_length=50, verbose_name='设备类型')
    sscj = models.ForeignKey(Sbcj, default='', verbose_name='所属厂家')
    sbdj = models.CharField(max_length=50, default='', null=True, verbose_name='设备等级')

    class Meta:
        verbose_name = '设备字典'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.sbxh

# 医院入组情况表
class Rzxx(models.Model):
    yymc=models.ForeignKey(Yyxx, null=True, verbose_name='医院名称')
    # sbcj=models.CharField(max_length=50, null=True, verbose_name='设备厂家')
    sbcj=models.ForeignKey(Sbcj, null=True, verbose_name='设备厂家')
    sbxh=models.ForeignKey(Sbxh, max_length=50, verbose_name='设备型号')
    # rzsj=models.DateTimeField(auto_now_add=True, verbose_name='入组时间')
    bz=models.TextField(max_length=500, null=True, verbose_name='备注')
    rzsj = models.DateTimeField(verbose_name='入组时间')
    class Meta:
        verbose_name='入组信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.yymc


class Market(models.Model):
    name = models.CharField(max_length=255)


class Security(models.Model):
    name = models.CharField(max_length=255)
    market = models.ForeignKey(Market)


class SecurityGroup(models.Model):
    name = models.CharField(max_length=255)
    market = models.ForeignKey(Market)
    # securities = models.ManyToManyField(Security)
    securities = models.ManyToManyField(Security, blank=True)