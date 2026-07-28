def __str__(self):...
atoms = []
for value, key, field in self._path:
if value is NotSupplied:
return '.'.join(atoms)
atoms.append(field)
if key is NotSupplied:
atoms.append('{}[{}]'.format(field, value))
atoms.append('{}{{{}={}}}'.format(field, key, value))
