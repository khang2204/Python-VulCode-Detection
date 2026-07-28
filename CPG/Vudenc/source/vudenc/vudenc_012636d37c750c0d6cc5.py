def get_new_uuid(uuid_, uuid_list=None):...
"""docstring"""
if not uuid_:
uuid_ = uuid.uuid4().hex
return uuid_
if type(uuid_list) in [set, dict]:
while uuid_ in uuid_list:
uuid_ = uuid.uuid4().hex
