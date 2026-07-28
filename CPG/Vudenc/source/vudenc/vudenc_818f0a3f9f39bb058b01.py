def test_yaml_file_path():...
native = {'foo': 'bar'}
source = yaml.dump(native)
tmp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.yaml')
tmp_file.write(source)
tmp_file.flush()
result = load_source(tmp_file.name)
assert result == native
