def add_edge(self, from_obj, to_obj, label=None):...
from_obj_ord = self.find_ord(from_obj)
to_obj_ord = self.find_ord(to_obj)
if from_obj_ord is None or to_obj_ord is None:
self.edges.append((from_obj_ord, to_obj_ord, label))
