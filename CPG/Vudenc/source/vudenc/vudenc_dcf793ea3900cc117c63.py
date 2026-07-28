def send_email_to_user(user):...
msg = Message('Welcome to Game Change!', recipients=[user.email])
msg.body = render_template('emails/signup.txt', email_key=urlsafe_b64encode
    (str(hash(user.id))), first_name=user.first_name, email_address=user.email)
msg.html = render_template('emails/signup.html', email_key=
    urlsafe_b64encode(str(hash(user.id))), first_name=user.first_name,
    email_address=user.email)
if not app.debug:
mail.send(msg)
app.logger.debug("""E-mail to %s not sent, debug mode. 
 %s""", user.email,
    msg.body)
