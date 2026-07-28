import unittest
import simplejson as json
from webtest import TestApp
from cornice.tests.validationapp import main, _json
from cornice.schemas import Errors
def test_validation(self):...
app = TestApp(main({}))
app.get('/service', status=400)
res = app.post('/service', params='buh', status=400)
self.assertTrue('Not a json body' in res.body)
res = app.post('/service', params=json.dumps('buh'))
self.assertEqual(res.body, json.dumps({'body': '"buh"'}))
app.get('/service?paid=yup')
res = app.get('/service?foo=1&paid=yup')
self.assertEqual(res.json['foo'], 1)
res = app.get('/service?foo=buh&paid=yup', status=400)
errors = Errors.from_json(res.body)
self.assertEqual(len(errors), 1)
apidocs = app.app.registry.settings['apidocs']
self.assertTrue(_json in apidocs['/service', 'POST']['validators'])
def test_accept(self):...
app = TestApp(main({}))
res = app.get('/service2', headers={'Accept': 'audio/*'}, status=406)
self.assertTrue('application/json' in res.json)
self.assertTrue('text/json' in res.json)
app.get('/service2', headers={'Accept': 'application/*'}, status=200)
app.get('/service2', headers={'Accept': 'audio/*, application/*'}, status=200)
res = app.get('/service3', headers={'Accept': 'audio/*'}, status=406)
self.assertTrue('text/json' in res.json)
app.get('/service3', headers={'Accept': 'text/*'}, status=200)
app.get('/service2', status=200)
def test_filters(self):...
app = TestApp(main({}))
self.assertTrue('filtered response' in app.get('/filtered').body)
self.assertTrue('unfiltered' in app.post('/filtered').body)
