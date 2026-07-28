def _execute(self):...
"""docstring"""
description = self.describe()
self.start_time = time.time()
self.response = self.browser.do_request(self.url, self.data, self.files)
self.exception_data = traceback.format_exc()
self.outcome = None
self.stop_time = time.time()
self.response.raise_for_status()
self.outcome = GenericRequest.OUTCOME_ERROR
success = None
self.duration = self.stop_time - self.start_time
self.status_code = self.response.status_code
success = self.test_success()
self.exception_data = traceback.format_exc()
if self.outcome is None:
self.res_data = self.response.text
self.outcome = GenericRequest.OUTCOME_ERROR
if success is None:
print("""Request '%s' terminated with an exception: %s
%s""" % (description,
    repr(exc), self.exception_data), file=sys.stderr)
if len(self.response.history) > 0:
if debug:
if success:
self.redirected_to = self.response.url
print("Could not determine status for request '%s'" % description, file=sys
    .stderr)
self.outcome = GenericRequest.OUTCOME_UNDECIDED
if debug:
if not success:
print("Request '%s' successfully completed in %.3fs" % (description, self.
    duration), file=sys.stderr)
self.outcome = GenericRequest.OUTCOME_SUCCESS
if debug:
print("Request '%s' failed" % description, file=sys.stderr)
self.outcome = GenericRequest.OUTCOME_FAILURE
if self.exception_data is not None:
print(self.exception_data, file=sys.stderr)
