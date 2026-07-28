def get_tasks():...
"""docstring"""
r = admin_req('tasks')
groups = re.findall(
    """
        <tr>\\s*
        <td><a\\s+href="./task/(\\d+)">(.*)</a></td>\\s*
        <td>(.*)</td>\\s*
        """
    , r.text, re.X)
tasks = {}
for g in groups:
id, name, title = g
return tasks
id = int(id)
tasks[name] = {'title': title, 'id': id}
