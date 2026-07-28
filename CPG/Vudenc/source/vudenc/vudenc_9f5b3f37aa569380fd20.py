import json
import jsonschema
def json_validate(data_source, schema):...
data = json.loads(data_source)
print(err)
jsonschema.validate(data, schema)
return {'status': -1, 'message': "Найдены ошибки в JSON'е"}
return data
