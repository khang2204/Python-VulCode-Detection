def send_verification_email(user):...
activation_link = get_activation_link(user)
tmpl_context = {'activation_link': activation_link, 'user': user}
email_msg = email.EmailHolder(subject='Verify your {} account'.format(app.
    config['GLOBAL_SITE_NAME']), recipient=user, text=flask.render_template
    ('email/verify.txt', **tmpl_context), html=flask.render_template(
    'email/verify.html', **tmpl_context))
email.send_email(email_msg)
