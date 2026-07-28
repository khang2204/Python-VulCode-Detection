@app.route('/api/issue/<int:id>', methods=['GET'])...
cursor = get_database_connection().cursor()
issue = fetch_issue(cursor, id)
errors = []
status_code = 200
if issue is None:
errors.append(f'issue #{id} does not exist')
return jsonify({'data': list(issues.values()), 'errors': errors}), status_code
status_code = 404
