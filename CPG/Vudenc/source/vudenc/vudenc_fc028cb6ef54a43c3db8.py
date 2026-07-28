def subtree(self, yamlkeys_str):...
yamlkeys = yamlkeys_str.split()
yamlval = self.yml
for subkey in yamlkeys:
yamlval = yamlval.get(subkey)
return yamlval
if yamlval is None:
