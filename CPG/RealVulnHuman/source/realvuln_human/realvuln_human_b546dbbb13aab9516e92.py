else:
        with Session() as session:
            current_user.profile_image = get_base64_image_blob(
                form.url.data).encode()
            session.merge(current_user)
            session.commit()

    return redirect('/account')


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
