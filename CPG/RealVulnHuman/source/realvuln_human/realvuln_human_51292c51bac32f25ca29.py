@app.route('/login', methods=['POST'])
def do_login():
    form = LoginForm(request.form)

    if not form.validate():
        flash(dumps(form.errors), 'error')
    else:
        with Session() as session:
            user = session.query(User).filter(
                User.email == form.email.data).first()
            if user is not None and checkpw(
                    form.password.data.encode('utf-8'),
                    user.password.encode('utf-8')) and login_user(user):
                return redirect("/")

    flash('Invalid Credentials!', 'warning')
    logout_user()

    return redirect("/")
