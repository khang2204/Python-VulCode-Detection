def authorization_error(self, error):...
logging.warning("""Authorization error.
%s
Peer: %s
IP: %s""", error, api.
    get_peer_identity().to_bytes(), self.request.remote_addr)
self.abort_with_error(403, text=str(error))
