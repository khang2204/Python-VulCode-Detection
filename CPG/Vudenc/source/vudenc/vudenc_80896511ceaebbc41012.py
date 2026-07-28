@app.route('/get_table_names', methods=['GET'])...
query = 'SELECT table_name FROM user_tables'
data = execute_query(app, g, query)[1]
return jsonify(data)
