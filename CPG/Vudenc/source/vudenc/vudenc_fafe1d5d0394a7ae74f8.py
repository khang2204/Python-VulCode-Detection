def _assert_provider(pid, purl):...
for provider in cluster_api.providers:
if provider.id == pid and provider.url == purl:
self.fail('Provider: %s not found' % pid)
return
