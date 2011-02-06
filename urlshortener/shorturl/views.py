# Create your views here.
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from shorturl.models import Url, Visitor
from shorturl.forms import ShortForm
from django.utils import simplejson
from django.contrib import messages
from django.core.urlresolvers import reverse


def home(request):
    form = ShortForm()
    return render_to_response('shorturl/home.html',
        locals(),
        context_instance=RequestContext(request))
    

def url_redirect(request, short_code):
    object = get_object_or_404(Url.objects.all(), short_code=short_code)
    if request.META.has_key('REMOTE_ADDR') and request.META.has_key('HTTP_USER_AGENT'):
        Visitor.objects.create(url = object, 
            remote_address = request.META['REMOTE_ADDR'],
            user_agent = request.META['HTTP_USER_AGENT']
            )
    return HttpResponsePermanentRedirect(object.long_url)

def shorten(request):
    if request.method == 'POST':
        form = ShortForm(request.POST)
        if request.user.is_authenticated():
            form.instance.user = request.user
        if request.is_ajax():
            if form.is_valid():
                form.save()
                data = {'status':'success',
                        'shor_code':form.instance.short_code}
            else:
                data = {'status':'error',
                        'error':form.errors}
            json = simplejson.dumps(data)
            return HttpResponse(json,mimetype="application/json")
        else:
            if form.is_valid():
                form.save()
                messages.success(request, 'Url was shorted')
            else:
                messages.error(request, 'Url not shorted')
                
    return render_to_response('shorturl/shorten.html',
        locals(),
        context_instance=RequestContext(request))        
                
    