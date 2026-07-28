def add_contest(**kwargs):...
add_args = {'name': kwargs.get('name'), 'description': kwargs.get(
    'description')}
resp = admin_req('contests/add', args=add_args)
page = resp.text
match = re.search(
    '<form enctype="multipart/form-data" action="../contest/([0-9]+)" method="POST" name="edit_contest" style="display:inline;">'
    , page)
if match is not None:
contest_id = int(match.groups()[0])
admin_req('contest/%s' % contest_id, args=kwargs)
return contest_id
