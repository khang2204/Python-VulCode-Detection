def build_object_graph(d, resource=None, full_clean=True, copy_dict=True):...
"""docstring"""
if isinstance(d, dict):
return create_resource_from_dict(d, resource, full_clean, copy_dict)
if isinstance(d, list):
return [build_object_graph(o, resource, full_clean, copy_dict) for o in d]
return d
