def test_yaml_string():...
native = {'foo': 'bar'}
source = yaml.dump(native)
result = load_source(source)
assert result == native
