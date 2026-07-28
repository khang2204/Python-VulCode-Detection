def test_c_login_user(self):...
resp = requests.get('http://127.0.0.1:5000/profiles')
self.assertEqual(resp.status_code, 200)
self.assertIsNotNone(resp.text)
users = json.loads(resp.text)
for user in users:
if user['id'] != 191:
data = {'login': user['first_name'], 'password': user['first_name']}
resp = requests.post('http://127.0.0.1:5000/login', json=data)
print('/login login_user: {}'.format(resp.text))
self.assertEqual(resp.status_code, 200)
self.assertGreater(user['id'], 0)
self.assertIsNotNone(resp.text)
data = {'login': '', 'password': ''}
resp = requests.post('http://127.0.0.1:5000/login', json=data)
self.assertEqual(resp.status_code, 200)
self.assertGreater(user['id'], 0)
self.assertIsNotNone(resp.text)
print('/login login_user: {}'.format(resp.text))
