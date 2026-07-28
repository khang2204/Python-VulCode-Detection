def test_native_mapping_is_passthrough():...
source = {'foo': 'bar'}
result = load_source(source)
assert result == source
