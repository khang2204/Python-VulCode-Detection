"""
Unit tests for the Deis api app.

Run the tests with "./manage.py test api\"
"""
from __future__ import unicode_literals
from django.test import TestCase
from deis import __version__
"""Tests middleware.py's business logic"""
fixtures = ['tests.json']
def setUp(self):...
self.assertTrue(self.client.login(username='autotest', password='password'))
def test_x_deis_version_header_good(self):...
"""docstring"""
response = self.client.get('/api/apps', HTTP_X_DEIS_VERSION=__version__.
    rsplit('.', 1)[0])
self.assertEqual(response.status_code, 200)
def test_x_deis_version_header_bad(self):...
"""docstring"""
response = self.client.get('/api/apps', HTTP_X_DEIS_VERSION='1234.5678')
self.assertEqual(response.status_code, 405)
def test_x_deis_version_header_not_present(self):...
"""docstring"""
response = self.client.get('/api/apps')
self.assertEqual(response.status_code, 200)
