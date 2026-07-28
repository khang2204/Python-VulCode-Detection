def test_admin_can_hook(self):...
"""docstring"""
"""Test creating a Push via the API"""
self.client.login(username='autotest2', password='password')
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
self.client.login(username='autotest', password='password')
DOCKERFILE = """
        FROM busybox
        CMD /bin/true
        """
body = {'receive_user': 'autotest', 'receive_repo': app_id, 'image':
    '{app_id}:v2'.format(**locals()), 'sha':
    'ecdff91c57a0b9ab82e89634df87e293d259a3aa', 'dockerfile': DOCKERFILE}
url = '/api/hooks/builds'
response = self.client.post(url, json.dumps(body), content_type=
    'application/json', HTTP_X_DEIS_BUILDER_AUTH=settings.BUILDER_KEY)
self.assertEqual(response.status_code, 200)
self.assertEqual(response.data['release']['version'], 2)
