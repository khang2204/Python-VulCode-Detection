def send_password_reset_request_email(user):...
"""docstring"""
reset_link = get_password_reset_link(user)
tmpl_context = {'reset_link': reset_link, 'user': user}
email_msg = email.EmailHolder(subject='{} password reset request'.format(
    app.config['GLOBAL_SITE_NAME']), recipient=user, text=flask.
    render_template('email/reset-request.txt', **tmpl_context), html=flask.
    render_template('email/reset-request.html', **tmpl_context))
email.send_email(email_msg)
