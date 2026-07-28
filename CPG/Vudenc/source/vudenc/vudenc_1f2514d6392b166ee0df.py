def test_b_get_user(self):...
resp = requests.get('http://127.0.0.1:5000/profiles')
self.assertEqual(resp.status_code, 200)
self.assertIsNotNone(resp.text)
print('/profiles get_user: {}'.format(resp.text))
users = json.loads(resp.text)
for user in users:
resp = requests.get('http://127.0.0.1:5000/profile/{}'.format(user['id']))
response = json.loads(resp.text)
print('/profile/{} get_user: {}'.format(user['id'], response))
self.assertEqual(resp.status_code, 200)
self.assertIsNotNone(resp.text)
self.assertGreater(response['id'], 0)
