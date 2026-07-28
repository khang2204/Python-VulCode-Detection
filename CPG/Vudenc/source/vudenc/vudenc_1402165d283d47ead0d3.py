def HandleGet(self):...
"""docstring"""
url = self.request.get('url').strip()
build_info = buildbot.ParseBuildUrl(url)
if not build_info:
return {'data': {'success': False}}
master_name, builder_name, build_number = build_info
cl_status = int(self.request.get('status'))
cl_info = self.request.get('cl_info')
user_name = users.get_current_user().email().split('@')[0]
success = _UpdateSuspectedCLAndAnalysis(master_name, builder_name,
    build_number, cl_info, cl_status, user_name)
return {'data': {'success': success}}
