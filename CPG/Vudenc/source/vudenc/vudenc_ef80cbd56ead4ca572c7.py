def allowed(self, request, keypair=None):...
if super(CreateKeyPair, self).allowed(request, keypair):
self.verbose_name = _('Create Key Pair')
return True
