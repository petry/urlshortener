# -*- coding: utf-8 -*-
# Autor: Marcos Daniel Petry - <marcospetry@gmail.com>
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UserChangeForm(forms.ModelForm):
    """
    Form to change User Data
    """
    username = forms.RegexField(label=_("Username"), max_length=30, regex=r'^[\w.@+-]+$',
        help_text = _("Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."),
        error_messages = {'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']