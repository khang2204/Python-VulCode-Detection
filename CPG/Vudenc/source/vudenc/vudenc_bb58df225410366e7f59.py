def test_add_user(self):...
for _ in range(3):
string = ''.join([chr(random.randint(65, 90)) for _ in range(9)])
data = {'first_name': string, 'second_name': string, 'login': string,
    'password': string}
print(data)
resp = requests.post('http://127.0.0.1:5000/register', json=data)
print(resp.text)
response = json.loads(resp.text)
self.assertEqual(resp.status_code, 200)
self.assertEqual(response['status'], 1)
print('/register test_add_user: {}'.format(resp.text))
