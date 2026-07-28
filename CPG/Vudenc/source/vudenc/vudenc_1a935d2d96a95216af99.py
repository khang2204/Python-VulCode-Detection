@staticmethod...
"""docstring"""
sql = ("select * from users where id = {0} and projects_mapped @> '{{{1}}}'"
    .format(user_id, project_id))
result = db.engine.execute(sql)
if result.rowcount > 0:
return
sql = (
    """update users
                    set projects_mapped = array_append(projects_mapped, {0})
                  where id = {1}"""
    .format(project_id, user_id))
db.engine.execute(sql)
