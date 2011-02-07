# -*- coding: utf-8 -*-
# Autor: Marcos Daniel Petry - <marcospetry@gmail.com>
from django import forms
from shorturl.models import Url
from django.conf import settings

class ShortForm(forms.ModelForm):
   
    class Meta:
        model = Url
        
    class Media:
        js = ('%sjs/short_script.js' % settings.MEDIA_URL,)
