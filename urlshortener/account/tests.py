

from django.test import TestCase
from shorturl.converter import base62_urlsafe
from django.test.client import Client
from shorturl.models import Url
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class RequestTest(TestCase):
    fixtures = ['account/fixtures/test_users.json', 'shorturl/fixtures/test_urls.json']
    
    def setUp(self):
        self.client = Client() 
     
        
    def test_signup(self):
        #annonymous user
        response = self.client.get(reverse('auth-signup'))
        self.assertEqual(response.status_code,200)
        
        #signup sucessful
        users = User.objects.count()
        response = self.client.post(reverse('auth-signup'), 
            {'username': 'testX', 'password1': 'x', 'password2':'x'})
        self.assertRedirects(response=response, 
            expected_url="%s" % reverse('auth-login') )
        self.assertEqual(User.objects.count(), users + 1)
            

        #wrong password
        response = self.client.post(reverse('auth-signup'), 
            {'username': 'testX', 'password1': 'x', 'password2':'xxxx'})
        self.assertFalse(response.context['form'].is_valid())
        self.assertEqual(response.status_code,200)
    
    
    def test_edit(self):
        #annonymous user
        response = self.client.get(reverse('auth-edit'))
        self.assertRedirects(response=response, 
            expected_url="%s?next=%s" % (reverse('auth-login'), reverse('auth-edit')))

        self.client.login(username='user1', password='b')
        response = self.client.get(reverse('auth-edit'))
        self.assertEqual(response.status_code,200)




        
    



