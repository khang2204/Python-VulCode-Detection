def test_get_env_properties_by_group(self):...
response = self.client.get(self.get_info_url, {'info_type':
    'env_properties', 'env_group_id': self.group_new.pk})
group = EnvGroup.objects.get(pk=self.group_new.pk)
expected_json = json.loads(serializers.serialize('json', group.property.all
    (), fields=('name', 'value')))
self.assertJSONEqual(str(response.content, encoding=settings.
    DEFAULT_CHARSET), expected_json)
