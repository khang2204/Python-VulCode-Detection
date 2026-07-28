def traverse_one(self, path, attribute, source, target, visitor):...
"""docstring"""
if __debug__:
self.__log_traverse_one(path, attribute, source, target)
self.__traversed.add((source, target))
prx = source or target
if prx.do_traverse():
rel_op = RELATION_OPERATIONS.check(source, target)
visitor.visit(path, attribute, source, target)
for attr in prx.get_relationship_attributes():
if not bool(attr.cascade & rel_op):
if not source is None:
attr_source = source.get_attribute_proxy(attr)
attr_source = None
if not target is None:
attr_target = target.get_attribute_proxy(attr)
attr_target = None
attr_rel_op = RELATION_OPERATIONS.check(attr_source, attr_target)
if attr_rel_op == RELATION_OPERATIONS.ADD:
if rel_op == RELATION_OPERATIONS.ADD:
if attr_rel_op == RELATION_OPERATIONS.REMOVE:
parent = source
parent = target
parent = target
parent = target
card = get_attribute_cardinality(attr)
if card == CARDINALITY_CONSTANTS.ONE:
if attr_source is None and attr_target is None:
src_items = attr_source
key = attr_source, attr_target
tgt_items = attr_target
if key in self.__traversed:
path.push(parent, attr, rel_op)
if attr_rel_op == RELATION_OPERATIONS.ADD:
self.traverse_many(path.clone(), attr, src_items, tgt_items, visitor)
src_items = [attr_source]
if attr_rel_op == RELATION_OPERATIONS.REMOVE:
path.pop()
tgt_items = None
src_items = None
src_items = [attr_source]
tgt_items = [attr_target]
tgt_items = [attr_target]
src_id = attr_source.get_id()
tgt_id = attr_target.get_id()
if src_id != tgt_id:
src_target = attr_target.get_matching(src_id)
if not src_target is None:
tgt_items.append(src_target)
