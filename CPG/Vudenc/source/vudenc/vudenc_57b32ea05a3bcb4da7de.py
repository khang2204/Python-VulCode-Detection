@gallery.route('/gallery/benwa/add', methods=['GET', 'POST'])...
form = PostForm()
if form.validate_on_submit():
f = form.image.data
flash('There was an issue with adding the benwa')
fname = secure_filename(f.filename)
return render_template('image_upload.html', form=form)
f.save(join(current_app.static_folder, current_app.config[
    'STATIC_BENWA_DIR'], fname))
fpath = '/'.join(['thumbs', fname])
created = datetime.utcnow()
preview = Preview(filepath=fpath, created=created)
db.session.add(preview)
fpath = '/'.join(['imgs', fname])
image = Image(filepath=fpath, created=created, preview=preview)
db.session.add(image)
tags = [Tag.query.get(1)]
added_tags = [get_or_create_tag(db.session, tag)[0] for tag in form.tags.
    data if tag]
tags.extend(added_tags)
post = Post(title=fname, created=datetime.utcnow(), image=image, tags=tags)
db.session.add(post)
current_user.posts.append(post)
db.session.commit()
return redirect(url_for('gallery.show_post', post_id=post.id))
