@bp.before_app_request...
if g.user:
if g.user['admin'] == 1:
posts = get_db().execute('SELECT * FROM post WHERE reviewed = 1').fetchall()
g.postcount = len(posts)
