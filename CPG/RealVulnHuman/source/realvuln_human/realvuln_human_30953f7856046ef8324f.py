@app.route('/unserialize', methods=['POST'])
def unserialize():
    import pickle
    data = request.data
    obj = pickle.loads(data)
    return str(obj)

# Vulnerability 4: Use of Outdated Library with Known Vulnerabilities
@app.route('/requests_example', methods=['GET'])
def requests_example():
    response = requests.get('https://example.com')
    return response.content

# Vulnerability 5: SQL Injection
@app.route('/user', methods=['GET'])
def get_user():
    user_id = request.args.get('id', '')
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    result = run_query(query)  # This function is not defined but simulates a database query
    return str(result)
