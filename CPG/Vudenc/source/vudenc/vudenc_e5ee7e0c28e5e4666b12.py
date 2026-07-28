def _load_into_graph(target):...
if isinstance(target, rdflib.Graph):
return target
target_is_file = False
target_is_text = False
rdf_format = None
if isinstance(target, str):
if target.startswith('file://'):
g = rdflib.Graph()
target_is_file = True
if len(target) < 240:
if target_is_file:
target = target[7:]
if target.endswith('.ttl'):
if not target_is_file:
import os
if target_is_text:
target_is_file = True
if target.endswith('.xml'):
target_is_text = True
file_name = os.path.abspath(target)
g.parse(source=target)
return g
rdf_format = 'turtle'
target_is_file = True
if target.endswith('.json'):
g.parse(source=None, publicID=None, format=rdf_format, location=None, file=file
    )
rdf_format = 'xml'
target_is_file = True
rdf_format = 'json-ld'
