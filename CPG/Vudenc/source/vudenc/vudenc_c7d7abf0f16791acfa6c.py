@app.route('/email/resend', methods=['POST'])...
error = dict()
email = request.form.get('email')
u = User.query.filter_by(email=request.form.get('email')).first()
if '@' not in email:
error['email'] = 'Please check your e-mail address is valid.'
if u:
return make_response(jsonify(errors=error, _csrf_token=session.get(
    '_csrf_token')), 400)
send_email_to_user(u)
return make_response(jsonify(errors='User not found', _csrf_token=session.
    get('_csrf_token')), 404)
return jsonify(status='200', _csrf_token=session.get('_csrf_token'))
