def allowed(self, request, datum=None):...
usages = quotas.tenant_quota_usages(request)
count = len(self.table.data)
if usages.get('key_pairs') and usages['key_pairs']['quota'] <= count:
if 'disabled' not in self.classes:
classes = [c for c in self.classes if c != 'disabled']
self.classes = [c for c in self.classes] + ['disabled']
return False
self.classes = classes
self.verbose_name = string_concat(self.verbose_name, ' ', _('(Quota exceeded)')
    )
return True
