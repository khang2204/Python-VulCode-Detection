def test_d_update_user(self):...
string = ''.join([chr(random.randint(33, 126)) for _ in range(9)])
resp = requests.get('http://127.0.0.1:5000/profiles')
self.assertEqual(resp.status_code, 200)
self.assertIsNotNone(resp.text)
users = json.loads(resp.text)
for user in users:
if user['id'] != 191:
data = {string: string, string: string}
resp = requests.put('http://127.0.0.1:5000/profile/{}'.format(user['id']),
    json=data)
response = json.loads(resp.text)
print(response)
self.assertEqual(resp.status_code, 200)
self.assertIsNotNone(resp.text)
self.assertEqual(response['status'], 0)
self.assertIsNotNone(response['message'])
print('[1] /profile/{} update_user: {}'.format(user['id'], resp.text))
resp = requests.get('http://127.0.0.1:5000/profile/{}'.format(user['id']),
    json=data)
response = json.loads(resp.text)
data = {'first_name': response['first_name'], 'second_name': string}
resp = requests.put('http://127.0.0.1:5000/profile/{}'.format(user['id']),
    json=data)
response2 = json.loads(resp.text)
self.assertEqual(resp.status_code, 200)
self.assertEqual(response2['status'], 1)
self.assertIsNotNone(response2['message'])
print('[2] /profile/{} update_user: {}'.format(user['id'], resp.text))
data = {'first_name': string + 'a', 'second_name': string + 'a'}
resp = requests.put('http://127.0.0.1:5000/profile/{}'.format(user['id']),
    json=data)
response = json.loads(resp.text)
self.assertEqual(resp.status_code, 200)
self.assertEqual(response['status'], 1)
print('[3] /profile/{} update_user: {}'.format(user['id'], resp.text))
