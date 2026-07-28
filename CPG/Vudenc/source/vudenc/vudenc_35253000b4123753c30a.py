def flow_for_request(self):...
"""docstring"""
flow = copy(self.flow)
flow.redirect_uri = url_for('oidc_callback', _external=True)
return flow
