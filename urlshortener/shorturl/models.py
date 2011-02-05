from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from shorturl.converter import base62_urlsafe



class Url(models.Model):
    long_url = models.URLField(max_length=4096)
    short_code = models.CharField(max_length=10, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    data_added = models.DateTimeField(auto_now_add=True, editable=False)
    clicks = models.PositiveIntegerField(editable=False, default=0)


class Visitor(models.Model):
    url = models.ForeignKey(Url)
    data_access = models.DateTimeField(auto_now_add=True, editable=False)
    remote_address = models.CharField(max_length=15)
    user_agent = models.CharField(max_length=150)



def add_code(signal, instance, sender, **kwargs):
    if not instance.short_code:
        instance.short_code = base62_urlsafe.encode(instance.id)
        instance.save()
    
post_save.connect(add_code, sender=Url)
    
        

