# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *


urlpatterns = patterns('django.contrib.auth.views',
     url(r'^login/$', 'login', name='auth-login')
    ,url(r'^logout/$', 'logout', {'next_page': "/"}, name='auth-logout')
    ,url(r'^password/change/$', 'password_change', name='auth-pass-change')
    ,url(r'^password/change/done/$', 'password_change_done', name='auth-pass-change-done')
    ,url(r'^password/reset/$', 'password_reset', name='auth-pass-reset')
    ,url(r'^password/reset/done/$', 'password_reset_done', name='auth-pass-reset-done')
    ,url(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm', name='auth-pass-reset-confirm')
    ,url(r'^password/reset/complete/$', 'password_reset_complete', name='auth-pass-reset-complete')

)
urlpatterns += patterns('account.views',
    url(r'^edit/$', 'edit', name='auth-edit'),
    url(r'^signup/$', 'signup', name='auth-signup')
)


