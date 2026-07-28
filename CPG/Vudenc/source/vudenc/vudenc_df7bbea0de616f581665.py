@decorators.require_cronjob...
"""docstring"""
host_url = 'https://%s.appspot.com' % app_identity.get_application_id()
request_id_url = host_url + '/restricted/ereporter2/request/'
report_url = host_url + '/restricted/ereporter2/report'
recipients = self.request.get('recipients', acl.get_ereporter2_recipients())
result = ui._generate_and_email_report(utils.get_module_version_list(None, 
    False), recipients, request_id_url, report_url, {})
self.response.headers['Content-Type'] = 'text/plain; charset=utf-8'
if result:
self.response.write('Success.')
self.response.write('Failed.')
