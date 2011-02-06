from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()




urlpatterns = patterns('',
    # Example:
    #(r'^midia/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,'show_indexes': True}),
    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^u/', include('account.urls')),
    (r'^', include('shorturl.urls')),

)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,'show_indexes': True}),
    )

