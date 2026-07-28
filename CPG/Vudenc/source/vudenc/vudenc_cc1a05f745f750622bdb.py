@memoized_property...
"""docstring"""
hasher = sha1()
for cp_entry in [self._zinc.zinc, self._zinc.compiler_interface, self._zinc
hasher.update(os.path.relpath(cp_entry, self.get_options().pants_workdir))
key = hasher.hexdigest()[:12]
return os.path.join(self.get_options().pants_bootstrapdir, 'zinc', key)
