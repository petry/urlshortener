from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class UserChangeForm(forms.ModelForm):
    username = forms.RegexField(label=_("Username"), max_length=30, regex=r'^[\w.@+-]+$',
        help_text = _("Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."),
        error_messages = {'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']