@gallery.route('/gallery/')...
if tags == 'all':
posts = Post.query.all()
split = tags.split(' ')
tags = Tag.query.all()
posts = []
return render_template('gallery.html', posts=posts, tags=tags)
for s in split:
results = Post.query.filter(Post.tags.any(name=s))
posts.extend(results)
