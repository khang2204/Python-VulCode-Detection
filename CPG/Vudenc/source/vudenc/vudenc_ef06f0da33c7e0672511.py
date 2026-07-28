import rdflib
import RDFClosure as owl_rl
from pyshacl.shape import find_shapes
if owl_rl.json_ld_available:
import rdflib_jsonld
import logging
logging.basicConfig()
log = logging.getLogger(__name__)
@classmethod...
options_dict['inference'] = True
options_dict['abort_on_error'] = False
@classmethod...
inferencer = owl_rl.DeductiveClosure(owl_rl.RDFS_OWLRL_Semantics)
log.error('Error during creation of OWL-RL Deductive Closure')
inferencer.expand(target_graph)
log.error('Error while running OWL-RL Deductive Closure')
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
def run(self):...
if self.options['inference']:
self._run_pre_inference(self.target_graph)
shapes = find_shapes(self.shacl_graph)
results = {}
for s in shapes:
r = s.validate(self.target_graph)
return results
results[s.node] = r
