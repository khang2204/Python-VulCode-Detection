def send_password_reset_email(user):...
"""docstring"""
email_msg = email.EmailHolder(subject='Your {} password has been reset'.
    format(app.config['GLOBAL_SITE_NAME']), recipient=user, text=flask.
    render_template('email/reset.txt', user=user), html=flask.
    render_template('email/reset.html', user=user))
email.send_email(email_msg)
