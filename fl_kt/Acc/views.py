#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
from models import *
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger

import logging


# Create your views here.

logger=logging.getLogger('Acc.views')


def global_setting(request):
    return {'SITE_NAME': settings.SITE_NAME,
            'SITE_DESC': settings.SITE_DESC,}


def index(request):

    try:
        # for a in Rzxx.objects.distinct_date():
        #     print a
        # -------------------------------------------
        # 归档栏目的数据列表动作
        Rzxx_list = Rzxx.objects.distinct_date()

        # 导航数据
        yy_list = Yyxx.objects.all()[:4]
        # 内容数据
        rz_list = Rzxx.objects.all()        # 获取数据集
        paginator = Paginator(rz_list, 2)  # 将数据集赋值给分页对象（每页5条）
        try:
            page = int(request.GET.get('page', 1))  # 获取当前页
            rz_list = paginator.page(page)           # 将当前页再传给列表变量
        except (EmptyPage, InvalidPage, PageNotAnInteger):  # 调用异常处理
            rz_list = paginator.page(1)
    except Exception as e:
        logger.error(e)
    # return render(request, 'index.html', {'yy_list': yy_list})
    # 在返回语句中的列表里添加：'article_list': article_list 就可以把变量传给页面模板
    # 但在实际使用中，{....}里的列表可以用locals()来代替：
    return render(request, 'index.html', locals())


# 定义归档函数
def archive_rzxx(request):
    try:
        # 先获取客户端提交的信息
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        # 分页
        rz_list = Rzxx.objects.filter(rzsj__icontains=year+'-'+month)  # 获取数据集（注意：前面是两个下划线_ _icontains中i表示忽略大小写，contains表示模糊查询)
        paginator = Paginator(rz_list, 2)  # 将数据集赋值给分页对象（每页5条）
        try:
            page = int(request.GET.get('page', 1))  # 获取当前页
            rz_list = paginator.page(page)  # 将当前页再传给列表变量
        except (EmptyPage, InvalidPage, PageNotAnInteger):  # 调用异常处理
            rz_list = paginator.page(1)

    except Exception as e:
        logger.error(e)

    return render(request, 'archive.html', locals())




