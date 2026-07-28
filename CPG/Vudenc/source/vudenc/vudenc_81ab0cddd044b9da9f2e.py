def json_dump(obj):...
import json
from core.libs.playhouse.shortcuts import model_to_dict
return json.loads(json.dumps(model_to_dict(obj, recurse=False), default=
    default, separators=(', ', ': '), indent=1))
