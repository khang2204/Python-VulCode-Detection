if username == USERNAME and password == PASSWORD:
        return "Login successful"
    else:
        return "Login failed", 401

# Vulnerability 3: Insecure Deserialization
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
