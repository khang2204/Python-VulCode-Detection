def find_oldest_node(self, filename):...
"""docstring"""
oldest_known_filename = filename
this_meta = NodeMetadata(filename)
if this_meta.get_tag('pulled from'):
oldest_known_filename = this_meta.get_tag('pulled from')[0].split(' |')[0
    ].strip(' ->')
return oldest_known_filename
return self.find_oldest_node(oldest_known_filename)
