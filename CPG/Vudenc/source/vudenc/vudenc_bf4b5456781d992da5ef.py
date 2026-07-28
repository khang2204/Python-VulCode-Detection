@gallery.route('/gallery/benwa/<int:post_id>')...
post = Post.query.paginate(post_id, 1, False)
if post.items:
return render_template('show.html', post=post, form=CommentForm())
flash("That Benwa doesn't exist yet")
return redirect(url_for('gallery.show_posts'))
