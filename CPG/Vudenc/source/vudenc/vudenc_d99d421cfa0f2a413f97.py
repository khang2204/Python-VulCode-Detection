def _fields_view_get(self, view_id=None, view_type='form', toolbar=False,...
"""docstring"""
result = super(ReadonlyViewMixin, self)._fields_view_get(view_id, view_type,
    toolbar, submenu)
readonly_fields = self.fields_get(attributes=['readonly'])
node = etree.fromstring(result['arch'])
for field in self._readonly_fields_to_add:
node.append(E.field(name=field, invisible='1'))
if not isinstance(self._readonly_domain, (list, tuple)):
lst_domain = [self._readonly_domain]
lst_domain = self._readonly_domain
self._process_field(node, readonly_fields, lst_domain)
result['arch'] = etree.tostring(node)
return result
