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

@app.route("/search", methods=["GET"])
def search():
    # Reflective XSS vulnerability
    query = request.args.get("q", "")
    return f"<h1>Search Results for {query}</h1>"

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000)
