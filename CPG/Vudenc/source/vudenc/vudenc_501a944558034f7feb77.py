def clean(self):...
cleaned_data = super(CreateKeypair, self).clean()
name = cleaned_data.get('name')
keypairs = api.nova.keypair_list(self.request)
exceptions.handle(self.request, ignore=True)
if name in [keypair.name for keypair in keypairs]:
keypairs = []
error_msg = _('The name is already in use.')
return cleaned_data
self._errors['name'] = self.error_class([error_msg])
