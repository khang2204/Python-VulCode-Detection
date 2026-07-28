def test_json_file_path():...
native = {'foo': 'bar'}
source = json.dumps(native)
tmp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json')
tmp_file.write(source)
tmp_file.flush()
result = load_source(tmp_file.name)
assert result == native
