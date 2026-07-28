print(request.form)
feedback = form_data.get('feedback', None)

error = ''
if not feedback:
    error = 'Please specify feedback to send'

if error:
    return render_template('account_area/account_area.html', error=error)
else:
    new_message = Message(message=feedback, from_user=current_user.username)
    db.session.add(new_message)
    db.session.commit()
    return render_template('account_area/account_area.html')
