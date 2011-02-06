# -*- coding: utf-8 -*-


from django.test import TestCase
from shorturl.converter import base62_urlsafe
from django.test.client import Client
from shorturl.models import Url
from django.core.urlresolvers import reverse


class ConverterTest(TestCase):
    def setUp(self):
        self.code1 = base62_urlsafe.encode('1234')
        self.code2 = base62_urlsafe.encode('4567')
        self.code3 = base62_urlsafe.encode('8901')
        
    
    def test_convert(self):
        self.assertEqual(base62_urlsafe.decode(self.code1),'1234')
        self.assertEqual(base62_urlsafe.decode(self.code2),'4567')
        self.assertEqual(base62_urlsafe.decode(self.code3),'8901')
        
        
class RequestTest(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_home(self):
        response = self.client.get(reverse('shorturl-home'))
        self.assertEqual(response.status_code,200)

    def test_shorten(self):
        """
        if request is ajax, process and show json feedback
        """
        response1 = self.client.post(reverse('shorturl-shorten'), 
            {'url': 'www.globo.com'})
        self.assertEqual(response1.status_code,200)

        
        
        response2 = self.client.post(reverse('shorturl-shorten'), 
            {'url': 'www.globo.com'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
 
        self.assertEqual(response2.status_code,200)
            

        
        
class RedirectTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url1 = Url.objects.create(long_url='http://petry.cc')
    
    def test_access_url(self):
        url = reverse('shorturl-urlredirect', args=[self.url1.short_code,])
        response = self.client.get(url, follow=True)
        self.assertRedirects(response=response, expected_url='http://petry.cc', status_code=301)



