def _session_send(request, **kwargs):...
if self._session_responses:
current_response = self._session_responses[0]
kwargs['allow_redirects'] = False
cluster_api.record_call(request, **kwargs)
return session_send(request, **kwargs)
return current_response() if hasattr(current_response, '__call__'
    ) else current_response
