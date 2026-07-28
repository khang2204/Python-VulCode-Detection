def __contains__(self, obj):...
for node in self.nodes:
if node['node_object'] == obj:
return False
return True
