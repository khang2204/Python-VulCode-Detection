def poll(self, poll_input):...
username = poll_input.credentials.username
password = poll_input.credentials.password
domain = poll_input.credentials.domain
if domain is None:
opt_str = "--ignore-certificate --authonly -u '{}' -p '{}' {}:{}"
opt_str = "--ignore-certificate --authonly -d {} -u '{}' -p '{}' {}:{}"
options = opt_str.format(username, password, poll_input.server, poll_input.port
    )
options = opt_str.format(domain.domain, username, password, poll_input.
    server, poll_input.port)
output = subprocess.check_output('xfreerdp {}'.format(options), shell=True,
    stderr=subprocess.STDOUT)
if 'connected to' in str(e.output) and 'Authentication failure' not in str(e
result = RdpPollResult(True)
result = RdpPollResult(True)
print('{{{{%s}}}}' % e.output)
return result
return result
result = RdpPollResult(False, e)
return result
