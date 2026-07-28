def verify_proper_post_request(req_data):...
"""docstring"""
if req_data is None:
return 0
user_info = req_data.get('userInfo', None)
if user_info is None:
return 1
fbid = user_info.get('fbid', None)
if fbid is None:
return 2
if type(fbid) == 'int':
return 3
return fbid
