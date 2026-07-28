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

def run_query(query):
    # Simulating a database query without proper sanitization (SQL Injection risk)
    return "Query result for: " + query

if __name__ == '__main__':
    app.run(debug=True)
