def test_rsa_key_str(self):...
"""docstring"""
url = '/api/keys'
body = {'id': 'autotest', 'public':
    'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDzqPAwHN70xsB0LXG//KzOgcPikyhdN/KRc4x3j/RA0pmFj63Ywv0PJ2b1LcMSqfR8F11WBlrW8c9xFua0ZAKzI+gEk5uqvOR78bs/SITOtKPomW4e/1d2xEkJqOmYH30u94+NZZYwEBqYaRb34fhtrnJS70XeGF0RhXE5Qea5eh7DBbeLxPfSYd8rfHgzMSb/wmx3h2vmHdQGho20pfJktNu7DxeVkTHn9REMUphf85su7slTgTlWKq++3fASE8PdmFGzb6PkOR4c+LS5WWXd2oM6HyBQBxxiwXbA2lSgQxOdgDiM2FzT0GVSFMUklkUHMdsaG6/HJDw9QckTS0vN autotest@deis.io'
    }
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
key = Key.objects.get(uuid=response.data['uuid'])
self.assertEqual(str(key),
    'ssh-rsa AAAAB3NzaC.../HJDw9QckTS0vN autotest@deis.io')
