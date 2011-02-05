# -*- coding: utf-8 -*-
# Autor: Marcos Daniel Petry - <marcospetry@gmail.com>
from django import forms
from django.forms import ModelForm
from shorturl.models import Url

class ShortForm(ModelForm):
   
    class Meta:
        model = Url