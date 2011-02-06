# -*- coding: utf-8 -*-
# Autor: Marcos Daniel Petry - <marcospetry@gmail.com>
from django import forms
from shorturl.models import Url

class ShortForm(forms.ModelForm):
   
    class Meta:
        model = Url