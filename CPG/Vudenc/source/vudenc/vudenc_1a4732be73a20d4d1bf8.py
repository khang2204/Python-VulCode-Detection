def get_users(contest_id):...
"""docstring"""
r = admin_req('contest/' + str(contest_id) + '/users')
groups = re.findall(
    """
        <tr> \\s*
        <td> \\s* (.*) \\s* </td> \\s*
        <td> \\s* (.*) \\s* </td> \\s*
        <td><a\\s+href="./user/(\\d+)">(.*)</a></td>
    """
    , r.text, re.X)
users = {}
for g in groups:
firstname, lastname, id, username = g
return users
id = int(id)
users[username] = {'firstname': firstname, 'lastname': lastname, 'id': id}
