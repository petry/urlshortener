from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from shorturl.converter import base62_urlsafe
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse


class Url(models.Model):
    long_url = models.URLField(max_length=4096, verify_exists=False)
    short_code = models.CharField(max_length=10, null=True, blank=True, editable=False)
    user = models.ForeignKey(User, null=True, blank=True, editable=False)
    data_added = models.DateTimeField(auto_now_add=True, editable=False)
    clicks = models.PositiveIntegerField(editable=False, default=0)
    
    class Meta:
        ordering = ['-data_added',]
        
    def short_url(self):
        current_site = Site.objects.get(id=settings.SITE_ID)
        return u"%s/%s" % (current_site.domain, self.short_code)
        
    def get_absolute_url(self):
        return reverse('shorturl-urldetail', args=[self.short_code])
        

class Access(models.Model):
    url = models.ForeignKey(Url)
    date_access = models.DateTimeField(auto_now_add=True, editable=False)
    remote_address = models.CharField(max_length=15)
    user_agent = models.CharField(max_length=150)



def add_code(signal, instance, sender, **kwargs):
    if not instance.short_code:
        instance.short_code = base62_urlsafe.encode(instance.id)
        instance.save()
    
post_save.connect(add_code, sender=Url)
    
        

