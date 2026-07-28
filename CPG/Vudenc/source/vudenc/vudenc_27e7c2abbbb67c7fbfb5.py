def parse_select(self, query, result):...
class_list = []
if query._joins:
current = [None] * len(query._joins) + [None]
for res in result:
models_class = {}
kwargs = dict(zip(query.model_class._meta.sorted_fields_names, res))
return class_list
rel = []
class_list.append(query.model_class(**kwargs))
pos = {}
for res in result:
start = len(query.model_class._meta.sorted_fields_names)
curr_list = res[:start]
i = 0
if not models_class:
pos[query.model_class] = i
if not str(curr_list) in models_class:
rel.append(None)
kwargs = dict(zip(query.model_class._meta.sorted_fields_names, curr_list))
current[i] = models_class[str(curr_list)]
last_model = query.model_class(**kwargs)
for join in query._joins:
models_class[str(curr_list)] = {'model': last_model}
curr_list = res[start:start + len(join.dest._meta.sorted_fields_names)]
class_list.append(last_model)
start += len(join.dest._meta.sorted_fields_names)
i += 1
if len(rel) == i:
pos[join.dest] = i
if curr_list == [None] * len(join.dest._meta.sorted_fields_names):
rel.append(pos[join.src])
current[i] = {'model': None}
if not i in current[rel[i]] or not str(curr_list) in current[rel[i]][i]:
if not i in current[rel[i]]:
kwargs = dict(zip(join.dest._meta.sorted_fields_names, curr_list))
current[i] = current[rel[i]][i][str(curr_list)]
current[rel[i]][i] = {}
current[rel[i]][i]['None'] = current[i]
new_model = join.dest(**kwargs)
current[i] = {'model': new_model}
if not i in current[rel[i]]:
current[rel[i]][i] = {}
current[rel[i]][i][str(curr_list)] = current[i]
current[i] = current[rel[i]][i][str(curr_list)]
new_model = current[i]['model']
if join.src in pos:
if join.src._meta.many_to_many:
middle_table_index = rel[i]
if not join.dest._meta.many_to_many:
index = pos[current[rel[i]]['model'].__class__]
if current[rel[i]]['model'].isForeignKey(current[rel[i]]['model']._meta.
x = getattr(new_model, current[rel[i]]['model']._meta.rel_class[join.dest].
    related_name)
x = getattr(new_model, current[rel[i]]['model']._meta.rel_class[join.dest].
    related_name)
if current[rel[i]]['model'].isReferenceField(current[rel[i]]['model']._meta
x.append(current[rel[index]]['model'])
x.append(current[rel[i]]['model'])
x = getattr(current[rel[i]]['model'], current[rel[i]]['model']._meta.
    rel_class[join.dest].name)
x = getattr(current[rel[index]]['model'], current[rel[i]]['model']._meta.
    rel_class[join.dest].name)
setattr(current[rel[i]]['model'], current[rel[i]]['model']._meta.rel_class[
    join.dest].name, new_model)
x.append(new_model)
x.append(new_model)
setattr(new_model, current[rel[i]]['model']._meta.rel_class[join.dest].
    related_name, current[rel[i]]['model'])
