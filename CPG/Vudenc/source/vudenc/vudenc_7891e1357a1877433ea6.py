def test_list_answers(self):...
response = self.client.get('/api/v1/questions/answers', headers={
    'Authorization': 'JWT ' + self.token})
self.assertEqual(response.status_code, 200)
self.assertEqual(response.get_json()['status'], 'success')
