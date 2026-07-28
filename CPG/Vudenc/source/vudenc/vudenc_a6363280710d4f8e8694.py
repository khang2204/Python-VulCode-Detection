def authentication_error(self, error):...
"""docstring"""
logging.warning("""Authentication error.
%s""", error)
self.abort(401, detail=str(error))
