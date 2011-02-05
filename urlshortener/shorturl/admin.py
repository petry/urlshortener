#!/usr/bin/env python
# encoding: utf-8
from django.contrib import admin
from django import forms
from shorturl.models import Url, Visitor



class VisitorInline(admin.TabularInline):
    model = Visitor
    readonly_fields = ['url', 'data_access', 'remote_address', 'user_agent']
    extra = 0
    max_num = 0 
    can_delete = False

class UrlAdmin(admin.ModelAdmin):
    model = Url
    list_display = ['id', 'long_url', 'short_code', 'clicks']
    readonly_fields = ['short_code', 'user']
    inlines = [VisitorInline, ]


admin.site.register(Url, UrlAdmin)

