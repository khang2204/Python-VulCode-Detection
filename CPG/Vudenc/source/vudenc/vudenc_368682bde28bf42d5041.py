def load_source(source):...
"""docstring"""
if isinstance(source, collections.Mapping):
return source
if hasattr(source, 'read') and callable(source.read):
raw_source = source.read()
if os.path.exists(os.path.expanduser(str(source))):
return json.loads(raw_source)
return yaml.load(raw_source)
raw_source = source_file.read()
if isinstance(source, six.string_types):
parts = urlparse.urlparse(source)
if parts.scheme and parts.netloc:
response = requests.get(source)
raw_source = source
if isinstance(response.content, six.binary_type):
raw_source = six.text_type(response.content, encoding='utf-8')
raw_source = response.content
