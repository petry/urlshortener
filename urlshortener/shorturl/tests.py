# -*- coding: utf-8 -*-


from django.test import TestCase
from shorturl.converter import base62_urlsafe
from django.test.client import Client
from shorturl.models import Url
from django.core.urlresolvers import reverse


class ConverterTest(TestCase):        
    
    def test_convert(self):
        self.code1 = base62_urlsafe.encode('1234')
        self.code2 = base62_urlsafe.encode('4567')
        self.code3 = base62_urlsafe.encode('8901')
        
        self.assertEqual(base62_urlsafe.decode(self.code1),'1234')
        self.assertEqual(base62_urlsafe.decode(self.code2),'4567')
        self.assertEqual(base62_urlsafe.decode(self.code3),'8901')
        
        
class RequestTest(TestCase):
    fixtures = ['shorturl/fixtures/test_users.json', 'shorturl/fixtures/test_urls.json']
    
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
    
    
    def test_detail(self):
        
        #annonymous user
        response = self.client.get(reverse('shorturl-urldetail', args=['C']))
        self.assertRedirects(response=response, 
            expected_url="%s?next=/C/details" % reverse('auth-login'), )

        #user1
        self.client.login(username='user1', password='b')
        response = self.client.get(reverse('shorturl-urldetail', args=['C']))
        self.assertEqual(response.status_code,200)
        self.assertEqual(Url.objects.get(short_code='C'), response.context['object'])

        
        #redirect
        response = self.client.get(reverse('shorturl-urldetail', args=['E']))
        self.assertRedirects(response=response, 
            expected_url=reverse('shorturl-home') )
        

        
class RedirectTest(TestCase):
    fixtures = ['shorturl/fixtures/test_users.json', 'shorturl/fixtures/test_urls.json']
    
    def setUp(self):
        self.client = Client()
    
    def test_access_url(self):
        #force 404 error
        response = self.client.get(reverse('shorturl-urlredirect', args=['XXXX']))
        self.assertEqual(response.status_code,404)
              
        url = reverse('shorturl-urlredirect', args=['C',])
        response = self.client.get(url, follow=True)
        self.assertRedirects(response=response, expected_url='http://petry.cc/', status_code=301)

        url = reverse('shorturl-urlredirect', args=['D',])
        response = self.client.get(url, follow=True)
        self.assertRedirects(response=response, expected_url='http://www.globo.com/', status_code=301)

        url = reverse('shorturl-urlredirect', args=['E',])
        response = self.client.get(url, follow=True)
        self.assertRedirects(response=response, expected_url='http://www.yahoo.com/', status_code=301)



