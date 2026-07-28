"""
Unit tests for the Deis api app.

Run the tests with "./manage.py test api\"
"""
from __future__ import unicode_literals
import json
from django.test import TestCase
from api.models import Key
from api.utils import fingerprint
RSA_PUBKEY = (
    'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfQkkUUoxpvcNMkvv7jqnfodgs37M2eBOAPgLK+KNBMaZaaKB4GF1QhTCMfFhoiTW3rqa0J75bHJcdkoobtTHlK8XUrFqsquWyg3XhsTYr/3RQQXvO86e2sF7SVDJqVtpnbQGc5SgNrHCeHJmf5HTbXSIjCO/AJSvIjnituT/SIAMGeBw0Nq/iSltwYAek1hiKO7wSmLcIQ8U4A00KEUtalaumf2aHOcfjgPfzlbZGP0S0cuBwSqLr8b5XGPmkASNdUiuJY4MJOce7bFU14B7oMAy2xacODUs1momUeYtGI9T7X2WMowJaO7tP3GlsgBMP81VfYTfYChAyJpKp2yoP autotest@autotesting comment'
    )
ECDSA_PUBKEY = (
    'ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBCGB0x9lmubbLJTF5NekCI0Cgjyip6jJh/t/qQQi1LAZisbREBJ8Wy+hwSn3tnbf/Imh9X+MQnrrza0jaQ3QUAQ= autotest@autotesting comment'
    )
"""Tests cloud provider credentials"""
fixtures = ['tests.json']
def setUp(self):...
self.assertTrue(self.client.login(username='autotest', password='password'))
def _check_key(self, pubkey):...
"""docstring"""
url = '/api/keys'
body = {'id': 'mykey@box.local', 'public': pubkey}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
key_id = response.data['id']
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
url = '/api/keys/{key_id}'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(body['id'], response.data['id'])
self.assertEqual(body['public'], response.data['public'])
response = self.client.delete(url)
self.assertEqual(response.status_code, 204)
def test_rsa_key(self):...
self._check_key(RSA_PUBKEY)
def test_ecdsa_key(self):...
self._check_key(ECDSA_PUBKEY)
def _check_duplicate_key(self, pubkey):...
"""docstring"""
url = '/api/keys'
body = {'id': 'mykey@box.local', 'public': pubkey}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 400)
def test_rsa_duplicate_key(self):...
self._check_duplicate_key(RSA_PUBKEY)
def test_ecdsa_duplicate_key(self):...
self._check_duplicate_key(ECDSA_PUBKEY)
def test_rsa_key_str(self):...
"""docstring"""
url = '/api/keys'
body = {'id': 'autotest', 'public':
    'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDzqPAwHN70xsB0LXG//KzOgcPikyhdN/KRc4x3j/RA0pmFj63Ywv0PJ2b1LcMSqfR8F11WBlrW8c9xFua0ZAKzI+gEk5uqvOR78bs/SITOtKPomW4e/1d2xEkJqOmYH30u94+NZZYwEBqYaRb34fhtrnJS70XeGF0RhXE5Qea5eh7DBbeLxPfSYd8rfHgzMSb/wmx3h2vmHdQGho20pfJktNu7DxeVkTHn9REMUphf85su7slTgTlWKq++3fASE8PdmFGzb6PkOR4c+LS5WWXd2oM6HyBQBxxiwXbA2lSgQxOdgDiM2FzT0GVSFMUklkUHMdsaG6/HJDw9QckTS0vN autotest@deis.io'
    }
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
key = Key.objects.get(uuid=response.data['uuid'])
self.assertEqual(str(key),
    'ssh-rsa AAAAB3NzaC.../HJDw9QckTS0vN autotest@deis.io')
def test_rsa_key_fingerprint(self):...
fp = fingerprint(RSA_PUBKEY)
self.assertEquals(fp, '54:6d:da:1f:91:b5:2b:6f:a2:83:90:c4:f9:73:76:f5')
