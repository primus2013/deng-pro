# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *

# Register your models here.


class RzxxAdmin(admin.ModelAdmin):
    fields = ('rzsj','yymc','sbcj','sbxh','bz',)
    # fields = ('yymc', 'sbcj', 'sbxh', 'bz',)
    # 在类中引入富媒体文件

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',

        )


class AdminSecurityGroup(admin.ModelAdmin):
    object = None

    def get_object(self, request, object_id):
        self.object = super(AdminSecurityGroup, self).get_object(request, object_id)
        return self.object

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name.lower() == 'securities':
            if self.object and self.object.market:
                kwargs['queryset'] = Security.objects.filter(market=self.object.market)
            else:
                kwargs['queryset'] = EmptyQuerySet()
        return super(AdminSecurityGroup, self).formfield_for_manytomany(db_field, request, **kwargs)




admin.site.register(User)
admin.site.register(Yyxx)
admin.site.register(Rzxx, RzxxAdmin)
admin.site.register(Sbcj)
admin.site.register(Sbxh)
