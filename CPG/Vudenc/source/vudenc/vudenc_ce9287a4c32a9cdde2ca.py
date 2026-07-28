@app.route('/manage/articles', methods=['GET', 'POST'])...
if current_user.is_authenticated:
createform = ArticleCreateForm()
return redirect('/index')
if createform.validate_on_submit():
article = Article(body=createform.body.data, url=createform.url.data,
    imageurl=createform.imageurl.data, author=current_user)
results = get_table_dict('Article')
db.session.add(article)
return render_template('managearticles.html', title='Manage Articles',
    createform=createform, items=results)
db.session.commit()
flash('Posted!')
return redirect('/manage/articles')
