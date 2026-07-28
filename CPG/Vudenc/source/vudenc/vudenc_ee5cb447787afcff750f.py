@gallery.route('/gallery/benwa/<int:post_id>/comment/add', methods=['POST'])...
form = CommentForm()
if form.validate_on_submit():
post = Post.query.get(post_id)
return redirect(url_for('gallery.show_post', post_id=post_id))
comment = Comment(content=form.content.data, created=datetime.utcnow(),
    user=current_user, post=post)
db.session.add(comment)
db.session.commit()
