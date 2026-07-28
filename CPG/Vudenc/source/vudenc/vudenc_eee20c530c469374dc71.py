def __init__(self, target_graph, *args, shacl_graph=None, options=None, **...
if options is None:
options = {}
self._load_default_options(options)
self.options = options
assert isinstance(target_graph, rdflib.Graph
    ), 'target_graph must be a rdflib Graph object'
self.target_graph = target_graph
if shacl_graph is None:
shacl_graph = target_graph
assert isinstance(shacl_graph, rdflib.Graph
    ), 'shacl_graph must be a rdflib Graph object'
self.shacl_graph = shacl_graph
