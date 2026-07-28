"""
Unit tests for the Deis api app.

Run the tests with "./manage.py test api\"
"""
from __future__ import unicode_literals
import json
import os.path
from django.test import TestCase
from django.conf import settings
from api.models import App
"""Tests creation of applications"""
fixtures = ['tests.json']
def setUp(self):...
self.assertTrue(self.client.login(username='autotest', password='password'))
settings.SSH_PRIVATE_KEY = '<some-ssh-private-key>'
def tearDown(self):...
settings.SSH_PRIVATE_KEY = ''
def test_app(self):...
"""docstring"""
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
self.assertIn('id', response.data)
self.assertIn('url', response.data)
self.assertEqual(response.data['url'], '{app_id}.deisapp.local'.format(**
    locals()))
response = self.client.get('/api/apps')
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
url = '/api/apps/{app_id}'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
body = {'id': 'new'}
response = self.client.patch(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 405)
response = self.client.delete(url)
self.assertEqual(response.status_code, 204)
def test_app_override_id(self):...
body = {'id': 'myid'}
response = self.client.post('/api/apps', json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
body = {'id': response.data['id']}
response = self.client.post('/api/apps', json.dumps(body), content_type=
    'application/json')
self.assertContains(response, 'App with this Id already exists.',
    status_code=400)
return response
