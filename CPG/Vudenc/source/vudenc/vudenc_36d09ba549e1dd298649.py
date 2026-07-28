def prepare_wildcard(value):...
if not isinstance(value, six.text_type):
value = six.text_type(value, 'utf-8', 'ignore')
value = six.text_type(unidecode(value))
parts = []
for item in value.split():
parts.append(item.lower() if item not in ('AND', 'OR', 'NOT') else item)
return ' '.join(parts)
