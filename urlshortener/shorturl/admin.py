# -*- coding: utf-8 -*-
# Autor: Marcos Daniel Petry - <marcospetry@gmail.com>from django import forms
from django.contrib import admin
from shorturl.models import Url, Access


class AccessInline(admin.TabularInline):
    model = Access
    readonly_fields = ['url', 'data_access', 'remote_address', 'user_agent']
    extra = 0
    max_num = 0 
    can_delete = False



class UrlAdmin(admin.ModelAdmin):
    model = Url
    list_display = ['id', 'long_url', 'short_code', 'clicks']
    readonly_fields = ['short_code', 'user']
    inlines = [AccessInline, ]


admin.site.register(Url, UrlAdmin)

