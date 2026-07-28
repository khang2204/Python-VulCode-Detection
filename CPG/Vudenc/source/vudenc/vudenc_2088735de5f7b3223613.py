def dispatch(self):...
"""docstring"""
conf = config.ensure_configured()
auth_context = api.reinitialize_request_cache()
self.response.headers['Content-Security-Policy'] = (
    "default-src https: 'self' 'unsafe-inline' https://www.google.com https://www.google-analytics.com 'unsafe-eval'"
    )
self.response.headers['Strict-Transport-Security'
    ] = 'max-age=31536000; includeSubDomains; preload'
if self.frame_options:
self.response.headers['X-Frame-Options'] = self.frame_options
identity = None
for method_func in self.get_auth_methods(conf):
self.auth_method = method_func
identity = method_func(self.request)
self.authentication_error(err)
identity = identity or model.Anonymous
if identity:
return
using_headers_auth = method_func in (oauth_authentication,
    service_to_service_authentication)
host_tok = self.request.headers.get(host_token.HTTP_HEADER)
if host_tok:
validated_host = host_token.validate_host_token(host_tok)
assert self.request.remote_addr
if validated_host:
ip = ipaddr.ip_from_string(self.request.remote_addr)
auth_context.peer_host = validated_host
auth_context.peer_ip = ip
auth_context.peer_identity = api.verify_ip_whitelisted(identity, ip, self.
    request.headers)
self.authorization_error(err)
delegation_tok = self.request.headers.get(delegation.HTTP_HEADER)
return
if delegation_tok:
auth_context.current_identity = auth_context.peer_identity
auth_context.current_identity = delegation.check_delegation_token(
    delegation_tok, auth_context.peer_identity)
self.authorization_error(api.AuthorizationError('Bad delegation token: %s' %
    exc))
need_xsrf_token = (not using_headers_auth and self.request.method in self.
    xsrf_token_enforce_on)
self.authorization_error(err)
msg = """Transient error while validating delegation token.
%s""" % exc
if need_xsrf_token and self.xsrf_token is None:
logging.error(msg)
self.xsrf_token_data = {}
self.abort(500, detail=msg)
if self.xsrf_token is not None:
self.xsrf_token_data = self.verify_xsrf_token()
super(AuthenticatingHandler, self).dispatch()
