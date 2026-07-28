PROFILE_PICTURES_UPLOAD_FOLDER = Config.PROFILE_PICTURES_UPLOAD_FOLDER
if not os.path.exists(PROFILE_PICTURES_UPLOAD_FOLDER):
    os.makedirs(PROFILE_PICTURES_UPLOAD_FOLDER)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# Handles user login.
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles user login.

    On GET request:
    Renders the login page.

    On POST request:
    Retrieves the username and password from the login form.
    Queries the database for the user based on the provided username.
    Checks if the provided password matches the hashed password stored in the database.
    If authentication succeeds, stores the username in the session and redirects to the dashboard.
    If authentication fails, renders the login page with an error message.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            return render_template('login.html', error='Please provide username and password')

        # Query the database for the user using parameterized query
        with get_db_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE username = ? OR email = ?"
            cursor.execute(query, (username,username))
            user = cursor.fetchone()

        # Check if the user exists and the password matches
        if user and user['password'] == custom_hash(password):
            session['username'] = user['username']
            session['user_id'] = user['id']

            # Update last_login timestamp
            cursor.execute("UPDATE users SET last_login = ? WHERE username = ?", (datetime.datetime.now(), username))
            conn.commit()
            conn.close()

            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

# Handles user registration.
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Handles user registration.

    On GET request:
    Renders the signup page.
