def _cfg(self, yamlkeys_str):...
yamlkeys = yamlkeys_str.split()
yamlval = self.yml
for subkey in yamlkeys:
yamlval = yamlval[subkey]
return yamlval
