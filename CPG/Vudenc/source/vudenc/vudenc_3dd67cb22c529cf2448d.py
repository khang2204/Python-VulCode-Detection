@bp.route('/')...
db = get_db()
postcount = g.postcount
pagecount = int(postcount / 5 + 1)
posts = db.execute(
    'SELECT * FROM post JOIN user WHERE post.uid = user.id AND post.reviewed = 1 ORDER BY created DESC LIMIT 5 OFFSET ?'
    , (str(page * 5),)).fetchall()
return render_template('admin/panel.html', posts=posts, pagecount=pagecount,
    page=page)
