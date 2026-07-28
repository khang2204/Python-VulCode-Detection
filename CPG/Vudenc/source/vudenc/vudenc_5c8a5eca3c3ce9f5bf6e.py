@rest_utils.ajax()...
"""docstring"""
console_type = request.DATA.get('console_type', 'AUTO')
CONSOLES = OrderedDict([('VNC', api.nova.server_vnc_console), ('SPICE', api
    .nova.server_spice_console), ('RDP', api.nova.server_rdp_console), (
    'SERIAL', api.nova.server_serial_console)])
"""Get a tuple of console url and console type."""
if console_type == 'AUTO':
check_consoles = CONSOLES
check_consoles = {console_type: CONSOLES[console_type]}
msg = _('Console type "%s" not supported.') % console_type
httpnotimplemented = exceptions.HttpNotImplemented
httpnotimplemented = exceptions.HTTPNotImplemented
for con_type, api_call in check_consoles.items():
console = api_call(request, server_id)
if con_type == 'SERIAL':
console_url = console.url
console_url = '%s&%s(%s)' % (console.url, utils_http.urlencode({'title': _(
    'Console')}), server_id)
return {'type': con_type, 'url': console_url}
