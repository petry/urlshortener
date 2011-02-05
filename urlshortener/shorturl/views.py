# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from shorturl.models import Url, Visitor

def short_url(request, short_code):
    object = get_object_or_404(Url.objects.all(), short_code=short_code)
    Visitor.objects.create(url = object, 
        remote_address = request.META['REMOTE_ADDR'],
        user_agent = request.META['HTTP_USER_AGENT']
        )
    
    
    return HttpResponseRedirect(object.long_url)
