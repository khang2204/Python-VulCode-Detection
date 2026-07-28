@inlineCallbacks...
"""docstring"""
if GLSetting.loglevel == logging.DEBUG and GLSetting.devel_mode:
return
uniform_delay = 0.8
request_time = self.request.request_time()
needed_diff = uniform_delay - request_time
if needed_diff > 0:
yield security_sleep(needed_diff)
