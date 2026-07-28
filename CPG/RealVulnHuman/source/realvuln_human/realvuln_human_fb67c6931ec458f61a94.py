return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Login Form """
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        passw = request.form['password']
        user = User.query.filter_by(username=name, password=passw).first()
        if user:
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            flash('Incorrect Login')
            return render_template('login.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    """ Register Form """
