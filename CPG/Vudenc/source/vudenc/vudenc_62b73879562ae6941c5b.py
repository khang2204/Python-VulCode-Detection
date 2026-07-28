def test_json_file_object():...
native = {'foo': 'bar'}
source = json.dumps(native)
tmp_file = tempfile.NamedTemporaryFile(mode='w')
tmp_file.write(source)
tmp_file.file.seek(0)
result = load_source(json_file)
assert result == native
