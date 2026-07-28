def test_json_string():...
native = {'foo': 'bar'}
source = json.dumps(native)
result = load_source(source)
assert result == native
