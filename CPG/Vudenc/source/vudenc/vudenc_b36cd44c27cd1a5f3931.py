def get_frontier_contexts(self, targetpath):...
"""docstring"""
"""
    
    implementation details:
    set of parameters:
    calculate extra parameters
    calculate missing parameters
    if there are missing parameters, then cull the search
    if there is one extra parameter, then add it to the hits
    if there is zero extra parameters, then continue
    if there is more than one extra parameters, then cull the search
    
    """
def __init__(self, targetctx, client):...
self._splitpath = fs.split_path(targetctx.path)
self._targetparam = set(targetctx.parameters.keys())
self._lensplitpath = len(self._splitpath)
self._store = {}
self._ds = client
def does_intersect_rule(self, rulectx):...
return True
