def test_e_del_user(self):...
resp = requests.get('http://127.0.0.1:5000/profiles')
self.assertEqual(resp.status_code, 200)
self.assertIsNotNone(resp.text)
users = json.loads(resp.text)
for user in users:
if user['id'] != 191:
resp = requests.delete('http://127.0.0.1:5000/profile/{}'.format(user['id']))
response = json.loads(resp.text)
self.assertEqual(resp.status_code, 200)
self.assertIsNotNone(resp.text)
self.assertEqual(response['status'], 1)
print('/profile/{} del_user: {}'.format(user['id'], resp.text))
