# Safe connection to the DB
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Safe retrieval of a selected post
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
