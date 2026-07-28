@app.route('/issues/', methods=['GET'])...
query = text('SELECT issue.id, issue.name FROM issue ORDER BY issue.name')
issues = db.engine.execute(query)
return render_template('/issues/list.html', current_user=current_user,
    issues=issues)
