cursor.execute("PRAGMA busy_timeout=10000;")  # Set busy timeout to 10 seconds (10000 ms)
        cursor.close()

# SECURITY VULNERABILITIES FOR EDUCATIONAL PURPOSES:
# 1. Intentionally vulnerable CORS configuration - DO NOT USE IN PRODUCTION
# 2. SQL Injection in transaction search - vulnerable endpoint at /api/transactions/search
# 3. Weak password hashing (MD5) in User model
# 4. Sensitive data exposure in user profiles

# Intentionally vulnerable CORS configuration - DO NOT USE IN PRODUCTION
@app.after_request
def after_request(response):
    # Reflect any origin in CORS headers - INSECURE!
    origin = request.headers.get('Origin')
    if origin:
        response.headers.add('Access-Control-Allow-Origin', origin)
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

# Initialize extensions
db.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(transaction_bp)

# Error handlers
@app.errorhandler(404)
