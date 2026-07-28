def filter(self, table, keypairs, filter_string):...
"""docstring"""
query = filter_string.lower()
return [keypair for keypair in keypairs if query in keypair.name.lower()]
