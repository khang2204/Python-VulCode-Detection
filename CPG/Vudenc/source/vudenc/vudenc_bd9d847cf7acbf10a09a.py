def test_container_state_good(self):...
"""docstring"""
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
c = Container.objects.create(owner=User.objects.get(username='autotest'),
    app=App.objects.get(id=app_id), release=App.objects.get(id=app_id).
    release_set.latest(), type='web', num=1)
self.assertEqual(c.state, 'initialized')
self.assertRaises(TransitionNotAllowed, lambda : c.start())
c.create()
self.assertEqual(c.state, 'created')
c.start()
self.assertEqual(c.state, 'up')
c.destroy()
self.assertEqual(c.state, 'destroyed')
