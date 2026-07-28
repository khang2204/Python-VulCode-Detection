@app.route('/signup', methods=['POST'])...
first_name = request.form.get('first_name')
last_name = request.form.get('last_name')
email = request.form.get('email')
user = User(first_name, last_name, email)
if user.isValid():
db.session.add(user)
resp = make_response(jsonify(errors=user.error, _csrf_token=session.get(
    '_csrf_token')), 400)
db.session.commit()
return resp
send_email_to_user(user)
return jsonify(status='200', _csrf_token=session.get('_csrf_token'))
