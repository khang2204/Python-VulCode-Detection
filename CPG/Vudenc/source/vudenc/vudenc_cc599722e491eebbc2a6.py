@mock.patch('requests.post', mock_import_repository_task)...
"""docstring"""
release3 = self.test_release()
release = Release.objects.get(uuid=release3['uuid'])
self.assertEqual(str(release), '{}-v3'.format(release3['app']))
