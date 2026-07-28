@staticmethod...
"""docstring"""
data = None
req = requests.post('https://api.dropbox.com/1/metadata/link', data=dict(
    link=DROPBOX_FOLDER_LINK, client_id=DROPBOX_APP_KEY, client_secret=
    DROPBOX_SECRET_KEY, path=filepath), timeout=5)
if req.ok:
req = json.loads(req.content.decode())['link'].split('?')[0] + '?dl=1'
data = None
req = requests.get(req, timeout=5)
data = None
return data
if req.ok:
data = req.content
