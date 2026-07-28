def setUp(self):...
super(TestNovaNetwork, self).setUp()
self.check_clients_state()
if not self.config.compute.compute_nodes:
self.skipTest('There are no compute nodes')
