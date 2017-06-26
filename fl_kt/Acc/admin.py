# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *

# Register your models here.


class RzxxAdmin(admin.ModelAdmin):
    # fields = ('yymc', 'sbcj', 'sbxh', 'rzsj', 'bz',)
    fields = ('yymc', 'sbcj', 'sbxh', 'bz',)
    # 在类中引入富媒体文件

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',

        )


admin.site.register(User)
admin.site.register(Yyxx)
admin.site.register(Rzxx, RzxxAdmin)
admin.site.register(Sbcj)
admin.site.register(Sbxh)
