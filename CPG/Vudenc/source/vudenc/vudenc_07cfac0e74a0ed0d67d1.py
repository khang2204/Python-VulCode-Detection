@app.route('/manage/posts/delete', methods=['POST'])...
if current_user.is_authenticated:
title = request.form.get('title')
return redirect('/index')
post = Post.query.filter_by(title=title).first()
db.session.delete(post)
db.session.commit()
return redirect('/manage/posts')
