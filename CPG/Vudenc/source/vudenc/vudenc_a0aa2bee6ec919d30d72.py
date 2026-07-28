def prepareData(data):...
"""docstring"""
allowed = data.get('allowedRolesAndUsers', None)
if allowed is not None:
data['allowedRolesAndUsers'] = [r.replace(':', '$') for r in allowed]
language = data.get('Language', None)
if language is not None:
if language == '':
searchable = data.get('SearchableText', None)
data['Language'] = 'any'
if isinstance(language, (tuple, list)) and '' in language:
if searchable is not None:
data['Language'] = [(lang or 'any') for lang in language]
if isinstance(searchable, dict):
path = data.get('path')
searchable = searchable['query']
if isinstance(searchable, six.binary_type):
if isinstance(path, dict) and not path.get('query'):
searchable = searchable.decode('utf-8')
if six.PY2:
data.pop('path')
searchable = searchable.encode('utf-8')
data['SearchableText'] = searchable.translate(translation_map)
if isinstance(data['SearchableText'], six.binary_type):
data['SearchableText'] = data['SearchableText'].decode('utf-8')
