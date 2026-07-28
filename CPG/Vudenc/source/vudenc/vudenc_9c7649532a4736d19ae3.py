@app.route('/api/issue', methods=['PUT'])...
connection = get_database_connection()
cursor = connection.cursor()
print(error)
return 'Not implemented.', 501
for issue in request.get_json().get('data', {}):
return jsonify({'error': str(error)}), 500
fetched_issue = fetch_issue(cursor, issue.get('id', -1))
if fetched_issue is None:
create_issue(cursor, issue)
if 'title' not in issue:
issue['title'] = ''
if 'description' not in issue:
issue['description'] = ''
if 'tags' not in issue:
issue['tags'] = []
update_issue(cursor, issue['id'], issue)
