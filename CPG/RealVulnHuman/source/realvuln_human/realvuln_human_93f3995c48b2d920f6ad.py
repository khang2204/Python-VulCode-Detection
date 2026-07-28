password = request.form.get("password")

    # SQL Injection Vulnerability
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    result = c.execute(query).fetchone()

    if result:
        response = make_response(redirect("/dashboard"))
        response.set_cookie("session", username)  # Insecure session management
        return response
    else:
        return "Invalid credentials. <a href='/'>Try again</a>"

@app.route("/dashboard")
def dashboard():
    # No authentication check
    user = request.cookies.get("session", "guest")
    return f"<h1>Welcome, {user}!</h1> <script>alert('XSS Vulnerability!')</script>"
