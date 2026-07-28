from __future__ import unicode_literals
import json
from django.test import TestCase
def test_first_signup(self):...
username, password = 'firstuser', 'password'
email = 'autotest@deis.io'
submit = {'username': username, 'password': password, 'email': email}
url = '/api/auth/register'
response = self.client.post(url, json.dumps(submit), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertTrue(response.data['is_superuser'])
username, password = 'seconduser', 'password'
email = 'autotest@deis.io'
submit = {'username': username, 'password': password, 'email': email}
url = '/api/auth/register'
response = self.client.post(url, json.dumps(submit), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertFalse(response.data['is_superuser'])
def test_list(self):...
submit = {'username': 'firstuser', 'password': 'password', 'email':
    'autotest@deis.io'}
url = '/api/auth/register'
response = self.client.post(url, json.dumps(submit), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertTrue(response.data['is_superuser'])
self.assertTrue(self.client.login(username='firstuser', password='password'))
response = self.client.get('/api/admin/perms', content_type='application/json')
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
self.assertEqual(response.data['results'][0]['username'], 'firstuser')
self.assertTrue(response.data['results'][0]['is_superuser'])
submit = {'username': 'seconduser', 'password': 'password', 'email':
    'autotest@deis.io'}
url = '/api/auth/register'
response = self.client.post(url, json.dumps(submit), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertFalse(response.data['is_superuser'])
self.assertTrue(self.client.login(username='seconduser', password='password'))
response = self.client.get('/api/admin/perms', content_type='application/json')
self.assertEqual(response.status_code, 403)
self.assertIn('You do not have permission', response.data['detail'])
def test_create(self):...
submit = {'username': 'first', 'password': 'password', 'email':
    'autotest@deis.io'}
url = '/api/auth/register'
response = self.client.post(url, json.dumps(submit), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertTrue(response.data['is_superuser'])
submit = {'username': 'second', 'password': 'password', 'email':
    'autotest@deis.io'}
url = '/api/auth/register'
response = self.client.post(url, json.dumps(submit), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertFalse(response.data['is_superuser'])
self.assertTrue(self.client.login(username='first', password='password'))
url = '/api/admin/perms'
body = {'username': 'second'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
self.assertIn('second', str(response.data['results']))
def test_delete(self):...
submit = {'username': 'first', 'password': 'password', 'email':
    'autotest@deis.io'}
url = '/api/auth/register'
response = self.client.post(url, json.dumps(submit), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertTrue(response.data['is_superuser'])
submit = {'username': 'second', 'password': 'password', 'email':
    'autotest@deis.io'}
url = '/api/auth/register'
response = self.client.post(url, json.dumps(submit), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertFalse(response.data['is_superuser'])
self.assertTrue(self.client.login(username='first', password='password'))
url = '/api/admin/perms'
body = {'username': 'second'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
response = self.client.delete(url + '/second')
self.assertEqual(response.status_code, 204)
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
self.assertNotIn('two', str(response.data['results']))
fixtures = ['test_sharing.json']
def setUp(self):...
self.assertTrue(self.client.login(username='autotest-1', password='password'))
def test_create(self):...
response = self.client.get('/api/apps')
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
app_id = response.data['results'][0]['id']
self.assertTrue(self.client.login(username='autotest-2', password='password'))
response = self.client.get('/api/apps')
self.assertEqual(len(response.data['results']), 1)
for model in ['builds', 'config', 'containers', 'limits', 'releases']:
response = self.client.get('/api/apps/{}/{}/'.format(app_id, model))
self.assertTrue(self.client.login(username='autotest-1', password='password'))
self.assertEqual(response.data['detail'], 'Not found')
url = '/api/apps/{}/perms'.format(app_id)
body = {'username': 'autotest-2'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertTrue(self.client.login(username='autotest-2', password='password'))
response = self.client.get('/api/apps')
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
for model in ['builds', 'containers', 'releases']:
response = self.client.get('/api/apps/{}/{}/'.format(app_id, model))
def test_create_errors(self):...
self.assertEqual(len(response.data['results']), 0)
response = self.client.get('/api/apps')
app_id = response.data['results'][0]['id']
self.assertTrue(self.client.login(username='autotest-2', password='password'))
url = '/api/apps/{}/perms'.format(app_id)
body = {'username': 'autotest-2'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 403)
def test_delete(self):...
self.assertTrue(self.client.login(username='autotest-1', password='password'))
response = self.client.get('/api/apps')
app_id = response.data['results'][0]['id']
url = '/api/apps/{}/perms'.format(app_id)
body = {'username': 'autotest-2'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertTrue(self.client.login(username='autotest-2', password='password'))
response = self.client.get('/api/apps')
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
url = '/api/apps/{}/perms/{}'.format(app_id, 'autotest-2')
response = self.client.delete(url, content_type='application/json')
self.assertEqual(response.status_code, 403)
self.assertIsNone(response.data)
self.assertTrue(self.client.login(username='autotest-1', password='password'))
response = self.client.delete(url, content_type='application/json')
self.assertEqual(response.status_code, 204)
self.assertIsNone(response.data)
self.assertTrue(self.client.login(username='autotest-2', password='password'))
response = self.client.get('/api/apps')
self.assertEqual(len(response.data['results']), 1)
self.assertTrue(self.client.login(username='autotest-1', password='password'))
response = self.client.delete(url, content_type='application/json')
self.assertEqual(response.status_code, 404)
def test_list(self):...
response = self.client.get('/api/apps')
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
app_id = response.data['results'][0]['id']
url = '/api/apps/{}/perms'.format(app_id)
body = {'username': 'autotest-2'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
response = self.client.get('/api/apps/{}/perms'.format(app_id),
    content_type='application/json')
self.assertEqual(response.data, {'users': ['autotest-2']})
def test_admin_can_list(self):...
"""docstring"""
response = self.client.get('/api/apps')
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
def test_list_errors(self):...
response = self.client.get('/api/apps')
app_id = response.data['results'][0]['id']
self.assertTrue(self.client.login(username='autotest-2', password='password'))
response = self.client.get('/api/apps/{}/perms'.format(app_id),
    content_type='application/json')
self.assertEqual(response.status_code, 403)
