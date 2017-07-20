# -*- coding: utf-8 -*-
# from __future__ import unicode_literals  #因为新建的归档日期格式化中的中文出错注释掉2017-7-15

from django.db import models

from django import forms





# Create your models here.

from django.contrib.auth.models import AbstractUser   # 此处是用户数据模型可以继承django已有的AbstractUser模型用（是一个关于用户的）

# 新建一个数据处理方法，将数据内容按日期归档

class RzxxManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []     # 存放处理结果
        date_list = self.values('rzsj')
        for date in date_list:
            # date = date['rzsj'].strftime('%Y{y}%m{m}').format(y='年', m='月')
            date = date['rzsj'].strftime('%Y/%m')
            # date = date['rzsj'].strftime('%Y/%m文件存档')  # 用于改变获得的数据格式
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list



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
    dengj = models.CharField(max_length=50, verbose_name='医院等级')
    yymc = models.CharField(max_length=50, verbose_name='医院名称')
    shengf = models.CharField(max_length=50, verbose_name='所在省份')
    # dengj = models.CharField(max_length=50, verbose_name='医院等级')

    class Meta:
        verbose_name = '医院字典'
        verbose_name_plural = verbose_name
        ordering = ['-yymc', 'dengj']

    def __unicode__(self):
        return self.yymc


# 厂家字典
class Sbcj(models.Model):
    cjmc = models.CharField(max_length=50, verbose_name='厂家名称')
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
    yymc=models.ForeignKey(Yyxx, verbose_name='医院名称')
    # sbcj=models.CharField(max_length=50, null=True, verbose_name='设备厂家')
    sbcj=models.ForeignKey(Sbcj, verbose_name='设备厂家')
    sbxh=models.ForeignKey(Sbxh, max_length=50, verbose_name='设备型号')
    # rzsj=models.DateTimeField(auto_now_add=True, verbose_name='入组时间')
    bz=models.TextField(max_length=500, null=True, verbose_name='备注')
    rzsj = models.DateTimeField(verbose_name='入组时间')

    # 将在models.py里定义的类关联进来
    objects = RzxxManager()

    class Meta:
        verbose_name='入组信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str('self.yymc')

# 文章模型
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=50, verbose_name='文章描述')
    content = models.TextField(verbose_name='文章内容')
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    # user = models.ForeignKey(User, verbose_name='用户')
    # category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类')
    # tag = models.ManyToManyField(Tag, verbose_name='标签')

    # objects = ArticleManager()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.title

# 评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    # username = models.CharField(max_length=30, blank=True, null=True, verbose_name='用户名')
    # email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='邮箱地址')
    # url = models.URLField(max_length=100, blank=True, null=True, verbose_name='个人网页地址')
    # date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    # user = models.ForeignKey(User, blank=True, null=True, verbose_name='用户')
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='文章')
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.id)



# class SumTS(models.Model):
#     sbjs = models.ForeignKey(Rzxx, verbose_name='设备计数')
#
#     class Meta:
#         verbose_name = '设备数量'
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return str('self.sbcj')

# 实验下拉联动
# ---------------------------------------
# Js方法实验

# class FooModel(models.Model):
#     province = models.CharField(max_length=50, verbose_name='省', choices=())
#     city= models.CharField(max_length=50, verbose_name='市', choices=())
#     area= models.CharField(max_length=50, verbose_name='区', choices=())

# ---------------------------------------
# 实验下拉联动方法二


# class Market(models.Model):
#     name = models.CharField(max_length=255)
#
#
# class Security(models.Model):
#     name = models.CharField(max_length=255)
#     market = models.ForeignKey(Market)
#
#
# class SecurityGroup(models.Model):
#     name = models.CharField(max_length=255)
#     market = models.ForeignKey(Market)
#     # securities = models.ManyToManyField(Security)
#     securities = models.ManyToManyField(Security, blank=True)
# ================================================
# 实验下拉联动方法三

# class FileType(models.Model):
#     name=models.CharField(max_length=128)
#
#     def __unicode__(self):
#         return self.name
#
#
# class ManagedFile(models.Model):
#     type = models.ForeignKey(FileType)
#     content = models.CharField(max_length=50)
#
#     def __unicode__(self):
#         return self.content
#
#
# class Tag(models.Model):
#     type = models.ForeignKey(FileType)
#     m_file = models.ForeignKey(ManagedFile)
#
#     def __unicode__(self):
#         return self.m_file
#
#     def clean(self):
#         if self.m_file is None:
#             return
#         if self.type != self.m_file.type:
#             raise forms.ValidationError("File type does not match Tag type")

