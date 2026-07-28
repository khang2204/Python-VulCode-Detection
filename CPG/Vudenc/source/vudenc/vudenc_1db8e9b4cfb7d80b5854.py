def __init__(self, name=None, port=None, gen_uuid=True):...
self.vars = {}
self.groups = []
self._uuid = None
self.name = name
self.address = name
if port:
self.set_variable('ansible_port', int(port))
if gen_uuid:
self._uuid = get_unique_id()
self.implicit = False
