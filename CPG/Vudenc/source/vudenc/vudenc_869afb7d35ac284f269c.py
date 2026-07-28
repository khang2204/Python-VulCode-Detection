def _exit(self, msg, error=1):...
"""docstring"""
self.log_error(msg)
self.close_all_connections()
sys.exit(error)
