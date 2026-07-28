def setUp(self):...
self.mail_service = mock()
self.services_factory = mock()
self.services_factory.mode = UserAgentMode(is_single_user=True)
self.services = mock()
self.services.mail_service = self.mail_service
self.services_factory._services_by_user = {'someuserid': self.mail_service}
when(self.services_factory).services(ANY()).thenReturn(self.services)
self.mail_service.account_email = self.MAIL_ADDRESS
root_resource = RootResource(self.services_factory)
root_resource._html_template = (
    '<html><head><title>$account_email</title></head></html>')
root_resource._mode = root_resource
self.web = DummySite(root_resource)
