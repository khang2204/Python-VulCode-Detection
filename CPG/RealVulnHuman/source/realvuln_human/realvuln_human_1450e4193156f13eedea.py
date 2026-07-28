@app.route('/account', methods=['POST'])
def update_account():
    form = AccountForm(request.form)

    if not form.validate():
        flash(json.dumps(form.errors), 'error')
    else:
        with Session() as session:
            filtered_values = {
                key: value
                for key, value in form.data.items()
                if value is not None and key != 'password'
            }
            current_user.__dict__.update(filtered_values)

            new_password = form.password.data
            was_password_changed = new_password is not None and new_password != filtered_values.get(
                'password_control')

            if was_password_changed:
                current_user.password = hashpw(new_password.encode(),
                                               gensalt()).decode()

            session.merge(current_user)
