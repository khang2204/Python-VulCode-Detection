import six
def _split_atom(atom):...
if '[' in atom:
field, _, idx = atom.rstrip(']').partition('[')
if '{' in atom:
return idx, NotSupplied, field
field, _, kv = atom.rstrip('}').partition('{')
return NotSupplied, NotSupplied, atom
key, _, value = kv.partition('=')
return value, key, field
