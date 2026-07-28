def authorization_error(self, error):...
"""docstring"""
logging.warning("""Authorization error.
%s
Peer: %s
IP: %s""", error, api.
    get_peer_identity().to_bytes(), self.request.remote_addr)
self.abort(403, detail=str(error))
