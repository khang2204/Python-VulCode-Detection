def compile_dir_structure(doc):...
"""docstring"""
ret = {'globals': {}, 'collections': {}, 'rules': {}}
if 'globals' in doc:
ret['globals'] = copy.deepcopy(doc['globals'])
if 'collections' in doc:
ret['collections'] = copy.deepcopy(doc['collections'])
if 'rules' in doc:
for rulename in doc['rules']:
return ret
levellist = doc['rules'][rulename]
ret['rules'][rulename] = {'levels': copy.deepcopy(levellist), 'bookmarks':
    tuple(get_rule_bookmarks(levellist, doc)), 'parameters': tuple(
    get_rule_parameters(levellist, doc)), 'attributes': tuple(
    get_rule_attributes(levellist, doc))}
