def get_post(post_id):
    conn = get_db_connection()  # SQL configured to schema.sql
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwerty12345'


# Bad: Vulnerable to SQL Injection
# Attempted Connection to the DB 
# And attempted retrieval of a post in the same function
# This can work
# But the example above proves simpler and doesn't need regex use
def get_db_connection():
    conn = get_db_connection()
 """
