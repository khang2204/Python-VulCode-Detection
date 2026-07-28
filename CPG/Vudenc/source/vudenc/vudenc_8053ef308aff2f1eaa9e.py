@functools.wraps(view)...
if g.user is None:
return redirect(url_for('auth.login'))
if g.user['admin'] != 1:
return redirect(url_for('blog.feedpage', page=0))
return view(**kwargs)
