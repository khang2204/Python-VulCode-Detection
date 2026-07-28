def allowed(self, request, keypair=None):...
if super(ImportKeyPair, self).allowed(request, keypair):
self.verbose_name = _('Import Key Pair')
return True
