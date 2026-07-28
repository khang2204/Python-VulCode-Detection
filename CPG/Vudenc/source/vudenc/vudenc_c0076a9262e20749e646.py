""" A simple implementation of a directed acyclic graph """
def __init__(self):...
self.nodes = []
self.edges = []
def __contains__(self, obj):...
for node in self.nodes:
if node['node_object'] == obj:
return False
return True
