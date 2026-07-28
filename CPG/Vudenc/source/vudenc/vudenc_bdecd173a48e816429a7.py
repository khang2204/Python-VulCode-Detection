def test_get_env_properties(self):...
response = self.client.get(self.get_info_url, {'info_type': 'env_properties'})
expected_json = json.loads(serializers.serialize('json', EnvProperty.
    objects.all(), fields=('name', 'value')))
self.assertJSONEqual(str(response.content, encoding=settings.
    DEFAULT_CHARSET), expected_json)
