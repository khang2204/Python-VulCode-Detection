def HandleGet(self):...
"""docstring"""
key_urlsafe = self.request.get('key').strip()
triage_result = self.request.get('triage_result')
if not key_urlsafe or triage_result is None:
return {'data': {'success': False}}
user_name = users.get_current_user().email().split('@')[0]
success = _UpdateSuspectedFlakeAnalysis(key_urlsafe, int(triage_result),
    user_name)
return {'data': {'success': success}}
