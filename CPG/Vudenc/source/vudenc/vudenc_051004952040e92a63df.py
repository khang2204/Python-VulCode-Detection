def load_list_from_json(json_file):...
json_obj = []
if os.path.exists(json_file):
json_obj = json.loads(ocf.read())
if not isinstance(json_obj, list):
return json_obj
