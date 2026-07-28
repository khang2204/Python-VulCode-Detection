@app.route('/manage/articles/update', methods=['POST'])...
if current_user.is_authenticated:
newbody = request.form.get('newbody')
return redirect('/index')
oldbody = request.form.get('oldbody')
newurl = request.form.get('newurl')
newimageurl = request.form.get('newimageurl')
article = Article.query.filter_by(body=oldbody).first()
article.body = newbody
article.url = newurl
article.imageurl = newimageurl
db.session.commit()
return redirect('/manage/articles')
