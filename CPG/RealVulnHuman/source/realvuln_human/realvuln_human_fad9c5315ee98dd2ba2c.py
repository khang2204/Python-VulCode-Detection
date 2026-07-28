@app.route('/signup', methods=['POST'])
def do_signup():
    form = RegistrationForm(request.form)

    if not form.validate():
        flash(dumps(form.errors), 'error')
    else:
        with Session() as session:
            user_already_exists = session.query(
                session.query(User).where(
                    User.email == form.email.data).exists()).scalar()

            code = form.registration_code.data
            token_id = validate_token(code, session)
            if token_id is None:
                flash("Invalid registration code", 'warning')
                return redirect("/signup")

            token = session.get(RegistrationCode, token_id)
            if token.code != code:
                flash("Unexpected registration code mismatch", 'error')
