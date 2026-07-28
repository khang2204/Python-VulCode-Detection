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
    app.run(host="0.0.0.0", port=80)
