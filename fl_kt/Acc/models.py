# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import  AbstractUser   #此处是用户数据模型可以继承django已有的AbstractUser模型用（是一个关于用户的）

class user(AbstractUser):
    avatar=models.ImageField(upload_to='avatar/%Y/%m',default='avatar/default.png',max_length=200, )
    qq=models.CharField(max_length=20,blank=True  ,null=True ,verbose_name='QQ号码')
    mobil=models.CharField(max_length=11,blank=True  ,null=True,unique=True ,verbose_name='手机号码')

    class meta:
        verbose_name='用户'
        verbose_nane_plural=verbose_name
        ordering=['-id']

        def __unicode__(self):
             return self.username



#
# # Create your models here.
# #医院入组情况表
# class rzxx(models.Model):
#     #yymc=models.CharField(max_length=50,verbose_name='医院名称')
#     yymc=models.ForeignKey(yyxx,verbose_name='医院名称')
#     sbcj=models.CharField(max_length= 50,verbose_name= '设备厂家')
#     sbxh=models.CharField(max_length= 50,verbose_name= '设备型号')
#     rzsj=models.DateTimeField(auto_now_add=True,verbose_name='入组时间')
#
#    class Meta:
#         verbose_name='医院名称'
#         verbose_name_plural=verbose_name
#
#         def __unicode__(self):
#             return self.yymc            #这里只能返回字符串，如果是数字，需要进行转换
#
# #医院字典
# class yyxx(models.Model):
#     yymc=models.CharField(max_length=50,verbose_name='医院名称')
#     shengf=models.CharField(max_length= 50,verbose_name= '所在省份')
#     dengj=models.CharField(max_length= 50,verbose_name= '医院等级')
#
#     class Meta:
#         verbose_name='医院名称'
#         verbose_name_plural=verbose_name
#
#         def __unicode__(self):
#             return self.yymc
#
# #厂家字典
# class sbcj(models.Model):
#     cjmc=models.CharField(max_length=50,verbose_name='厂家名称')
#     szdq=models.CharField(max_length= 50,verbose_name= '所在地区')
#
#     class Meta:
#         verbose_name='厂家名称'
#         verbose_name_plural=verbose_name
#
#         def __unicode__(self):
#             return self.cjmc
#
# #设备字典
# class sbxh(models.Model):
#     sbxh=models.CharField(max_length=50,verbose_name='设备型号')
#     leix=models.CharField(max_length= 50,verbose_name= '设备类型')
#
#     class Meta:
#         verbose_name='设备型号'
#         verbose_name_plural=verbose_name
#
#         def __unicode__(self):
#            return self.sbxh