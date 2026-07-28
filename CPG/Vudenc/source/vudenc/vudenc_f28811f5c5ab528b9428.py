"""
Unit tests for the Deis api app.

Run the tests with "./manage.py test api\"
"""
from __future__ import unicode_literals
import json
import mock
import requests
from django.test import TransactionTestCase
from django.conf import settings
def mock_import_repository_task(*args, **kwargs):...
resp = requests.Response()
resp.status_code = 200
resp._content_consumed = True
return resp
