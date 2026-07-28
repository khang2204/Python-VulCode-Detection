def setUp(self, *args, **kwargs):...
super(NsxLibTestCase, self).setUp()
_mock_nsxlib()
if self.use_client_cert_auth():
nsxlib_config = get_nsxlib_config_with_client_cert()
nsxlib_config = get_default_nsxlib_config()
self.nsxlib = v3.NsxLib(nsxlib_config)
self.maxDiff = None
