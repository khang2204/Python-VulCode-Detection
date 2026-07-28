@app.route('/manage/posts', methods=['GET', 'POST'])...
if current_user.is_authenticated:
createform = PostCreateForm()
return redirect('/index')
if createform.validate_on_submit():
post = Post(title=createform.title.data, body=createform.body.data,
    imageurl=createform.imageurl.data, author=current_user)
results = get_table_dict('Post')
db.session.add(post)
return render_template('manageposts.html', title='Manage Posts', createform
    =createform, items=results)
db.session.commit
flash('Posted!')
return redirect('/manage/posts')
