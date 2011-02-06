from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from shorturl.models import Url
from shorturl.forms import ShortForm
from django.utils import simplejson
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from account.forms import UserChangeForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('You are subscribed!'))
            return HttpResponseRedirect( reverse('auth-login') )
        else:
            messages.error(request, _('There was an error when signing up!') )
            
    else:
        form = UserCreationForm()
    return render_to_response('account/signup.html'
                             ,locals()
                             ,context_instance=RequestContext(request))
      
      
@login_required                       
def edit(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, _('Profile details updated.'))
            return HttpResponseRedirect(reverse('shorturl-home') )
        else:
            messages.error(request, _('There was an error when editing your data'))
            
    else:
        form = UserChangeForm(instance=request.user)
    return render_to_response('account/edit.html'
                             ,locals()
                             ,context_instance=RequestContext(request))

