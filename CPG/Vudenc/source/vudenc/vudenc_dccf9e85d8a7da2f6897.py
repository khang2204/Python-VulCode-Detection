@gallery.route('/gallery/benwa/<int:post_id>/comment/delete/<int:comment_id>',...
comment = Comment.query.get_or_404(comment_id)
if current_user.has_role('admin') or comment.owner(current_user):
db.session.delete(comment)
flash("you can't delete this comment")
db.session.commit()
return redirect(url_for('gallery.show_post', post_id=post_id))
