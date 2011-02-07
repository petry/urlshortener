# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from shorturl.models import Url, Access
from shorturl.forms import ShortForm
from django.utils import simplejson
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _


def home(request):
    form = ShortForm()

    
    return render_to_response('shorturl/home.html',
        locals(),
        context_instance=RequestContext(request))
    

def url_redirect(request, short_code):
    object = get_object_or_404(Url.objects.all(), short_code=short_code)
    if request.META.has_key('REMOTE_ADDR') and request.META.has_key('HTTP_USER_AGENT'):
        Access.objects.create(url = object, 
            remote_address = request.META['REMOTE_ADDR'],
            user_agent = request.META['HTTP_USER_AGENT']
            )
    return HttpResponsePermanentRedirect(object.long_url)


@login_required
def url_detail(request, short_code):
    object = get_object_or_404(Url.objects.all(), short_code=short_code)   
    if object.user != request.user: 
        messages.error(request, _('This URL no belont to you'))
        return HttpResponseRedirect(reverse('shorturl-home'))
        
    return render_to_response('shorturl/detail.html',
        locals(),
        context_instance=RequestContext(request))


from django.core import serializers

@login_required
def tabledata(request):
    object_list = Url.objects.filter(user=request.user)
    return render_to_response('shorturl/url_table.html',
        locals(),
        context_instance=RequestContext(request))
    
    

def shorten(request):
    if request.method == 'POST':
        form = ShortForm(request.POST)
        if request.user.is_authenticated():
            form.instance.user = request.user
        if request.is_ajax():
            if form.is_valid():
                form.save()
                data = {'status':'success',
                        'long_url':form.instance.long_url,
                        'short_url':form.instance.short_url()
                        }
            else:
                data = {'status':'error',
                        'error':form.errors}
            json = simplejson.dumps(data)
            return HttpResponse(json,mimetype="application/json")
        else:
            if form.is_valid():
                form.save()
                messages.success(request, _('Url was shorted'))
            else:
                messages.error(request, _('Url not shorted'))
                
    return render_to_response('shorturl/shorten.html',
        locals(),
        context_instance=RequestContext(request))        
                
    