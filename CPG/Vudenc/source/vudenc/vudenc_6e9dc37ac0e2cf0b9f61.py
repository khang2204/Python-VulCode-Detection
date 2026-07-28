def _assert_providers(self, cluster_api, provider_tuples):...
self.assertEqual(len(cluster_api.providers), len(provider_tuples))
def _assert_provider(pid, purl):...
for provider in cluster_api.providers:
if provider.id == pid and provider.url == purl:
self.fail('Provider: %s not found' % pid)
return
for provider_tuple in provider_tuples:
_assert_provider(provider_tuple[0], provider_tuple[1])
