if not (current_password and new_password and confirm_password):
        error = 'Please specify all fields'
    if not current_user.password == current_password:
        error = 'Current password incorrect'
    if not new_password == confirm_password:
        error = 'Password confirmation doesn\'t match'

    if error:
        return render_template('account_area/account_area.html', error=error)
    else:
        User.query.filter_by(id=current_user.id).update({
            'password': new_password
        })
        db.session.commit()
        return render_template('account_area/account_area.html')


@account_area.route('/change_email', methods=['POST'])
@login_required
def change_email():
    form_data = request.form
    new_email = form_data.get('email', None)
