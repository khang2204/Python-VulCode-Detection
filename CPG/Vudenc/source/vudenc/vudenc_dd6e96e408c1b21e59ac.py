def authentication_error(self, error):...
logging.warning("""Authentication error.
%s""", error)
self.abort_with_error(401, text=str(error))
