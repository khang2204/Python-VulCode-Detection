session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            flash('Incorrect Login')
            return render_template('login.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    """ Register Form """
    if request.method == 'POST':
        new_user = User(username=request.form['username'], password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route("/logout")
def logout():
    """ Logout Form """
    session['logged_in'] = False
    return redirect(url_for('home'))
