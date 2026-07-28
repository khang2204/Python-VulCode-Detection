def _validate_result(self, result, expected, operation, silent=False):...
if result.status_code not in expected:
result_msg = result.json() if result.content else ''
if not silent:
LOG.warning(
    'The HTTP request returned error code %(result)s, whereas %(expected)s response codes were expected. Response body %(body)s'
    , {'result': result.status_code, 'expected': '/'.join([str(code) for
    code in expected]), 'body': result_msg})
error_code = None
if isinstance(result_msg, dict) and 'error_message' in result_msg:
error_code = result_msg.get('error_code')
self._raise_error(result.status_code, operation, result_msg, error_code=
    error_code)
related_errors = [error['error_message'] for error in result_msg.get(
    'related_errors', [])]
result_msg = result_msg['error_message']
if related_errors:
result_msg += ' relatedErrors: %s' % ' '.join(related_errors)
