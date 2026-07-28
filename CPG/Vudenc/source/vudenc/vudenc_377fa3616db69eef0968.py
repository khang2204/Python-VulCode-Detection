@authn_views.route('/saml2-metadata')...
"""docstring"""
metadata = entity_descriptor(current_app.saml2_config)
response = make_response(metadata.to_string(), 200)
response.headers['Content-Type'] = 'text/xml; charset=utf8'
return response
