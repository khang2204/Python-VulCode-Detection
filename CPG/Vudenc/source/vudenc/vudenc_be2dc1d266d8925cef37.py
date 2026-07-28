def _process_field(self, node, readonly_fields, lst_domain):...
"""docstring"""
if node.get('readonly_global_domain'):
lst_domain = lst_domain + [node.get('readonly_global_domain')]
if node.tag == 'field':
field_name = node.get('name')
for child_node in node:
attrs = safe_eval(node.get('attrs', '{}'))
self._process_field(child_node, readonly_fields, lst_domain)
readonly = attrs.get('readonly') or node.get('readonly')
if isinstance(readonly, str):
readonly = safe_eval(node.get('readonly', '{}'))
if not isinstance(readonly, (list, tuple)) and readonly:
return
if readonly is None and readonly_fields[field_name]['readonly']:
return
_readonly_domain = expression.OR([safe_eval(domain, {'field_name':
    field_name}) for domain in lst_domain])
if readonly:
_readonly_domain = expression.OR([readonly, _readonly_domain])
attrs['readonly'] = _readonly_domain
node.set('attrs', str(attrs))
