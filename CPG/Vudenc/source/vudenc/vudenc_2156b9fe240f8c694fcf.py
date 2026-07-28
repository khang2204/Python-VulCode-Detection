@authn_views.route('/saml2-acs', methods=['POST'])...
"""docstring"""
if 'SAMLResponse' not in request.form:
abort(400)
xmlstr = request.form['SAMLResponse']
session_info = get_authn_response(current_app.config, session, xmlstr)
current_app.logger.debug('Trying to locate the user authenticated by the IdP')
user = authenticate(current_app, session_info)
if user is None:
current_app.logger.error('Could not find the user identified by the IdP')
action = get_action()
return action(session_info, user)
