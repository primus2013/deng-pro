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
        # 导航数据
        yy_list = Yyxx.objects.all()[:4]
        # 内容数据
        rz_list = Rzxx.objects.all()        # 获取数据集
        paginator = Paginator(rz_list, 5)  # 将数据集赋值给分页对象（每页5条）
        try:
            page = int(request.GET.get('page', 1))  # 获取当前页
            rz_list = paginator.page(page)           # 将当前页再传给列表变量
        except (EmptyPage, InvalidPage, PageNotAnInteger):  # 调用异常处理
            rz_list = paginator.page(1)
    except Exception as e:
        logger.error(e)
    # return render(request, 'index.html', {'yy_list': yy_list})
    #在返回语句中的列表里添加：'article_list': article_list 就可以把变量传给页面模板
    #但在实际使用中，{....}里的列表可以用locals()来代替：
    return render(request,'index.html',locals())
