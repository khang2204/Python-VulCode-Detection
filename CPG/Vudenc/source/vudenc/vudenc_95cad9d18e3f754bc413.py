def traverse_many(self, path, attribute, source_sequence, target_sequence,...
"""docstring"""
target_map = {}
if not target_sequence is None:
for target in target_sequence:
src_tgt_pairs = []
target_map[target.get_id()] = target
if not source_sequence is None:
for source in source_sequence:
for target in itervalues_(target_map):
source_id = source.get_id()
if not (None, target) in self.__traversed:
for source, target in src_tgt_pairs:
if not source_id is None:
self.traverse_one(path, attribute, None, target, visitor)
if not (source, target) in self.__traversed:
target = target_map.pop(source_id, None)
target = None
self.traverse_one(path, attribute, source, target, visitor)
src_tgt_pairs.append((source, target))
