# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *
from django import forms

# Register your models here.


class FooForm(forms.ModelForm):
    class Meta:
        model = FooModel
        fields = ('province', 'city', 'area',)
        widgets = {
            'province': forms.Select,
            'city': forms.Select,
            'area': forms.Select
        }


class FooAdmin(admin.ModelAdmin):
    form = FooForm

    class Media:

        js = (
            '/static/js/jsAddress.js',
            '/static/js/pca_init.js',
            '/static/js/jquery.min.js'
        )


class RzxxAdmin(admin.ModelAdmin):
    fields = ('rzsj','yymc','sbcj','sbxh','bz',)

    # 在类中引入富媒体文件

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
            '/static/js/jsAddress.js',
            '/static/js/pca_init.js',
        )


# 试验下拉联动
# class BlogArticleAdmin(admin.ModelAdmin):
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "sort_id":
#             kwargs["queryset"] = Tags.objects.filter(user=request.user)
#         return super(BlogArticleAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


def tagform_factory(filetype):

    class TagForm(forms.ModelForm):   # 需要增加from django import forms
        m_file = forms.ModelChoiceField(
            queryset=ManagedFile.objects.filter(type=filetype)
        )
    return TagForm


class TagAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        if obj is not None and obj.type is not None:
            kwargs['form'] = tagform_factory(obj.type)
        return super(TagAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Tag, TagAdmin)
admin.site.register(ManagedFile)
admin.site.register(FileType)

admin.site.register(User)
admin.site.register(Yyxx)
admin.site.register(Rzxx, RzxxAdmin)
admin.site.register(Sbcj)
admin.site.register(Sbxh)

admin.site.register(FooModel, FooAdmin)

