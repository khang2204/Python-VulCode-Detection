def _gitiles_slugify(value, _separator):...
"""docstring"""
value = value.encode('ascii', 'replace')
value = re.sub('[^- a-zA-Z0-9]', '_', value)
value = value.replace(u' ', u'-')
value = re.sub('([-_])[-_]+', '\\1', value)
return value
