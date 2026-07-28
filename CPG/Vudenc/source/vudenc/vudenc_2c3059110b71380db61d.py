def _apply_wildcards(newitems, olditems, wildcards, wildcards_obj,...
for name, item in olditems.allitems():
start = len(newitems)
is_iterable = True
if callable(item):
if not_iterable(item):
item = item(wildcards_obj)
if not_iterable(item):
item = [item]
for item_ in item:
item = [item]
for item_ in item:
is_iterable = False
concrete = concretize(item_, wildcards)
if name:
is_iterable = False
if not isinstance(item_, str):
newitems.append(concrete)
newitems.set_name(name, start, end=len(newitems) if is_iterable else None)
concrete = concretize(item_, wildcards)
if ruleio is not None:
newitems.append(concrete)
ruleio[concrete] = item_
if ruleio is not None:
ruleio[concrete] = item_
