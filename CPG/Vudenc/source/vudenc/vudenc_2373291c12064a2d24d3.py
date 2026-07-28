def log_out(self):...
"""docstring"""
logging.info('Using default log_out() method')
self.clear_session()
return self.redirect_to_goodbye()
