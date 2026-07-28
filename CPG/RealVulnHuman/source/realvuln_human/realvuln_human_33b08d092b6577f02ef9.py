def get_db_connection():
    conn = get_db_connection()
 """
  The problem: The regex filters values that begin and end with numbers only as indicated by \d
  also, re.M indicates a multi-line regex evaluation
  the post id is catted to the remaining query
"""
    num_format = re.compile(r'^\d+$', re.M) # weak regex
        if re.match(num_format,post_id):
        # SQLI vuln, passes user input to string
            post = conn.execute('SELECT * FROM posts WHERE id = '+post_id).fetchone()
            conn.close()
            if post is None:
                abort(404)
            return post
        else:
            abort(404)


@app.route('/')
def index():
