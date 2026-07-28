def test_yaml_file_object():...
native = {'foo': 'bar'}
source = yaml.dump(native)
tmp_file = tempfile.NamedTemporaryFile(mode='w')
tmp_file.write(source)
tmp_file.flush()
result = load_source(yaml_file)
assert result == native
