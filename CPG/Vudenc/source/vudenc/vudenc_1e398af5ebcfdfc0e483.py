def compare_node_to_regex(self, node):...
"""docstring"""
for regex in self.config['nodes']:
return False
regex = fnmatch.translate(regex)
msg = 'Error comparing %s to provided node regex %s: %s'
if re.match(regex, node):
self.log_debug(msg % (node, regex, err))
return True
