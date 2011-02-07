# -*- coding: utf-8 -*-
# Autor: Marcos Daniel Petry - <marcospetry@gmail.com>
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('shorturl.views',
    url(r'^$', 'home', name='shorturl-home'),
    url(r'^api/shorten/$', 'shorten', name='shorturl-shorten'),
    url(r'^api/data/$', 'tabledata', name='shorturl-tabledata'),
    url(r'^(?P<short_code>[\d\w]+)/$', 'url_redirect', name='shorturl-urlredirect'),
    url(r'^(?P<short_code>[\d\w]+)/details$', 'url_detail', name='shorturl-urldetail'),

)
