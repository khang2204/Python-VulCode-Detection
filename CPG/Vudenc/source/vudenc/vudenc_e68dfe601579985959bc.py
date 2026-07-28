def test_003_check_networks(self):...
"""docstring"""
seen_nets = self.verify(50, self._list_networks, 1,
    'List of networks is not available.', 'listing networks')
seen_labels, seen_ids = zip(*((n.label, n.id) for n in seen_nets))
for mynet in self.network:
self.verify_response_body(seen_labels, mynet.label,
    'Network can not be created.properly', failed_step=2)
self.verify_response_body(seen_ids, mynet.id,
    'Network can not be created. properly ', failed_step=3)
