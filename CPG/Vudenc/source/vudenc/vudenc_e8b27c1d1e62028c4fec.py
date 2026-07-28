@app.route('/manage/articles/delete', methods=['POST'])...
if current_user.is_authenticated:
body = request.form.get('body')
return redirect('/index')
article = Article.query.filter_by(body=body).first()
db.session.delete(article)
db.session.commit()
return redirect('/manage/articles')
