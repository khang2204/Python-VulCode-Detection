"""
Unit tests for the Deis api app.

Run the tests with "./manage.py test api\"
"""
from __future__ import unicode_literals
import json
from django.conf import settings
from django.test import TransactionTestCase
from scheduler import chaos
"""Tests creation of containers on nodes"""
fixtures = ['tests.json']
def setUp(self):...
self.assertTrue(self.client.login(username='autotest', password='password'))
chaos.CREATE_ERROR_RATE = 0
chaos.DESTROY_ERROR_RATE = 0
chaos.START_ERROR_RATE = 0
chaos.STOP_ERROR_RATE = 0
settings.SCHEDULER_MODULE = 'chaos'
settings.SSH_PRIVATE_KEY = '<some-ssh-private-key>'
def tearDown(self):...
settings.SCHEDULER_MODULE = 'mock'
settings.SSH_PRIVATE_KEY = ''
def test_create_chaos(self):...
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
url = '/api/apps/{app_id}/builds'.format(**locals())
body = {'image': 'autotest/example', 'sha': 'a' * 40, 'procfile': json.
    dumps({'web': 'node server.js', 'worker': 'node worker.js'})}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'web': 0}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 204)
chaos.CREATE_ERROR_RATE = 0.5
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'web': 20}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 503)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 20)
states = set([c['state'] for c in response.data['results']])
self.assertEqual(states, set(['error', 'created']))
def test_start_chaos(self):...
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
url = '/api/apps/{app_id}/builds'.format(**locals())
body = {'image': 'autotest/example', 'sha': 'a' * 40, 'procfile': json.
    dumps({'web': 'node server.js', 'worker': 'node worker.js'})}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'web': 0}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 204)
chaos.START_ERROR_RATE = 0.5
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'web': 20}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 204)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 20)
states = set([c['state'] for c in response.data['results']])
self.assertEqual(states, set(['crashed', 'up']))
def test_destroy_chaos(self):...
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
url = '/api/apps/{app_id}/builds'.format(**locals())
body = {'image': 'autotest/example', 'sha': 'a' * 40, 'procfile': json.
    dumps({'web': 'node server.js', 'worker': 'node worker.js'})}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'web': 20}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 204)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 20)
chaos.DESTROY_ERROR_RATE = 0.5
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'web': 0}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 503)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
states = set([c['state'] for c in response.data['results']])
self.assertEqual(states, set(['error']))
containers = 20
for _ in range(100):
url = '/api/apps/{app_id}/scale'.format(**locals())
def test_build_chaos(self):...
body = {'web': 0}
url = '/api/apps'
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
response = self.client.post(url)
if response.status_code == 204:
self.assertEqual(response.status_code, 201)
self.assertEquals(response.status_code, 503)
app_id = response.data['id']
url = '/api/apps/{app_id}/containers'.format(**locals())
url = '/api/apps/{app_id}/builds'.format(**locals())
response = self.client.get(url)
body = {'image': 'autotest/example', 'sha': 'a' * 40, 'procfile': json.
    dumps({'web': 'node server.js', 'worker': 'node worker.js'})}
self.assertEqual(response.status_code, 200)
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
containers = len(response.data['results'])
self.assertEqual(response.status_code, 201)
url = '/api/apps/{app_id}/builds'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
url = '/api/apps/{app_id}/releases'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'web': 20}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 204)
chaos.CREATE_ERROR_RATE = 0.5
chaos.START_ERROR_RATE = 0.5
url = '/api/apps/{app_id}/builds'.format(**locals())
body = {'image': 'autotest/example', 'sha': 'b' * 40, 'procfile': json.
    dumps({'web': 'node server.js', 'worker': 'node worker.js'})}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 503)
url = '/api/apps/{app_id}/releases'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 20)
states = set([c['state'] for c in response.data['results']])
self.assertEqual(states, set(['up']))
def test_config_chaos(self):...
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
url = '/api/apps/{app_id}/builds'.format(**locals())
body = {'image': 'autotest/example', 'sha': 'a' * 40, 'procfile': json.
    dumps({'web': 'node server.js', 'worker': 'node worker.js'})}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
url = '/api/apps/{app_id}/releases'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'web': 20}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 204)
chaos.CREATE_ERROR_RATE = 0.5
chaos.START_ERROR_RATE = 0.5
url = '/api/apps/{app_id}/config'.format(**locals())
body = {'values': json.dumps({'NEW_URL1': 'http://localhost:8080/'})}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 503)
url = '/api/apps/{app_id}/releases'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 20)
states = set([c['state'] for c in response.data['results']])
self.assertEqual(states, set(['up']))
def test_run_chaos(self):...
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
url = '/api/apps/{app_id}/builds'.format(**locals())
body = {'image': 'autotest/example', 'sha': 'a' * 40, 'procfile': json.
    dumps({'web': 'node server.js', 'worker': 'node worker.js'})}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
url = '/api/apps/{app_id}/builds'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
url = '/api/apps/{app_id}/releases'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
chaos.CREATE_ERROR_RATE = 1
url = '/api/apps/{app_id}/run'.format(**locals())
body = {'command': 'ls -al'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 503)
