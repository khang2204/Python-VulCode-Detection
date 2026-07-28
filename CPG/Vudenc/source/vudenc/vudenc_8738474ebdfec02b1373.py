def test_container_state_protected(self):...
"""docstring"""
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
c = Container.objects.create(owner=User.objects.get(username='autotest'),
    app=App.objects.get(id=app_id), release=App.objects.get(id=app_id).
    release_set.latest(), type='web', num=1)
self.assertRaises(AttributeError, lambda : setattr(c, 'state', 'up'))
