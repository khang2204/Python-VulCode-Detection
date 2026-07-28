def validate_host(host_key):...
"""docstring"""
if len(host_key) == 22 and host_key[16:22] == '.onion':
return True
hostchunk = str(host_key).split(':')
if len(hostchunk) == 2:
host_key = hostchunk[0]
if host_key in GLSetting.accepted_hosts:
return True
log.debug('Error in host requested: %s not accepted between: %s ' % (
    host_key, GLSetting.accepted_hosts))
return False
