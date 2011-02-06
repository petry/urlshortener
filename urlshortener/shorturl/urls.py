# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
urlpatterns = patterns('shorturl.views',
    url(r'^$', 'home', name='shorturl-home'),
    url(r'^api/shorten/$', 'shorten', name='shorturl-shorten'),


    url(r'^(?P<short_code>[\d\w]+)/$', 'url_redirect', name='shorturl-urlredirect'),

)
