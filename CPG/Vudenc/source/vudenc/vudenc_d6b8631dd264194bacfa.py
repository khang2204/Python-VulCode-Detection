def handle_error(self, err):...
"""docstring"""
understood = (KeyError, ValueError, TypeError, AttributeError,
    SQLAlchemyError, DokomoError)
if isinstance(err, tornado.web.HTTPError):
restless_error = exc.HttpError(err.log_message)
if isinstance(err, understood):
restless_error.status = err.status_code
err = exc.BadRequest(err)
return super().handle_error(err)
err = restless_error
