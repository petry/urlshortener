# -*- coding: utf-8 -*-
# Autor: Marcos Daniel Petry - <marcospetry@gmail.com>
from account.forms import UserChangeForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class RequestTest(TestCase):
    fixtures = ['account/fixtures/test_users.json', 'shorturl/fixtures/test_urls.json']
    
    def setUp(self):
        self.client = Client() 
     
        
    def test_signup(self):
        response = self.client.get(reverse('auth-signup'))
        self.assertEqual(response.status_code, 200)


    def test_signup_wrong_password(self):
        response = self.client.post(reverse('auth-signup'), 
            {'username': 'testX', 'password1': 'x', 'password2':'xxxx'})
        self.assertFalse(response.context['form'].is_valid())
        self.assertEqual(response.context['form'].errors,
                         {'password2': [u"The two password fields didn't match."]})
        self.assertEqual(response.status_code, 200)
        

    def test_signup_successful(self):
        users = User.objects.count()
        response = self.client.post(reverse('auth-signup'), 
            {'username': 'testX', 'password1': 'x', 'password2':'x'})
        self.assertRedirects(response=response, 
            expected_url="%s" % reverse('auth-login') )
        self.assertEqual(User.objects.count(), users + 1)
            
  
    def test_edit_annonymous(self):
        response = self.client.get(reverse('auth-edit'))
        self.assertRedirects(response=response, 
            expected_url="%s?next=%s" % (reverse('auth-login'), reverse('auth-edit')))


    def test_edit_authenticated(self):
        self.client.login(username='user1', password='b')
        response = self.client.get(reverse('auth-edit'))
        self.assertEqual(response.status_code, 200)



class UserChangeFormTest(TestCase):

    fixtures = ['account/fixtures/test_users.json']

    def test_username_validity(self):
        user = User.objects.get(username='user1')
        data = {'username': '$$$$$$$$'}
        form = UserChangeForm(data, instance=user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form['username'].errors,
                         [u'This value may contain only letters, numbers and @/./+/-/_ characters.'])

