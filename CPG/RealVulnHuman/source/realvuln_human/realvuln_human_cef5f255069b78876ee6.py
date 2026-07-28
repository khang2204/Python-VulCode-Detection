form_data = request.form
    new_email = form_data.get('email', None)

    error = ''
    if not new_email:
        error = 'Please specify an email'

    if error:
        return render_template('account_area/account_area.html', error=error)
    else:
        User.query.filter_by(id=current_user.id).update({
            'email': new_email
        })
        db.session.commit()
        return render_template('account_area/account_area.html')


@account_area.route('/send_feedback', methods=['POST'])
@login_required
def send_feedback():
    form_data = request.form
    print(request.form)
