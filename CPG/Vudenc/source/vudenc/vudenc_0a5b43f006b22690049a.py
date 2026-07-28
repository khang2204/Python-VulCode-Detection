@app.route('/<issue_id>/delete', methods=['POST'])...
if not current_user.is_admin:
return redirect(url_for('error401'))
issue_to_delete = Issue.query.get(issue_id)
if not issue_to_delete:
return redirect(url_for('error404'))
articles_in_issue = Article.query.filter_by(issue=issue_id)
for article in articles_in_issue:
article.set_issue(0)
db.session.delete(issue_to_delete)
db.session.commit()
return redirect(url_for('issues_index'))
