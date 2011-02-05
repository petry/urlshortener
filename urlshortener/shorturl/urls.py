# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
urlpatterns = patterns('shorturl.views',
   url(r'^(?P<short_code>[\d\w]+)/$', 'short_url', name='shorturl-url'),

)
