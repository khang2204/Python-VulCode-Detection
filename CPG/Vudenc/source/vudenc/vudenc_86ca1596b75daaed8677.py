@app.route('/api/issue', methods=['POST'])...
connection = get_database_connection()
for issue in request.get_json()['data']:
return jsonify({'data': [], 'errors': ['failed to create rows in sqlite',
    str(error)]}), 400
return 'Not implemented.', 501
create_issue(connection.cursor(), issue)
