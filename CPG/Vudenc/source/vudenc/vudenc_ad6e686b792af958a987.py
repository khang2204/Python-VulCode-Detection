def leap_mail(uid=0, flags=LEAP_FLAGS, headers=None, extra_headers={},...
fdoc = TestDoc({'flags': flags, 'mbox_uuid': mbox_uuid, 'type': 'flags',
    'uid': uid, 'chash': chash})
if headers is None:
headers = {}
if not (headers.get('received') or headers.get('date')):
headers.update(DEFAULT_HEADERS)
headers['headers'] = extra_headers
hdoc = TestDoc(headers)
bdoc = TestDoc({'raw': body, 'type': 'cnt'})
return fdoc, hdoc, bdoc
