@staticmethod...
origin = log_check_output(['git', 'remote', 'get-url', 'origin'],
    universal_newlines=True)[:-1]
commit = log_check_output(['git', 'log', '-1', '--format=%H'],
    universal_newlines=True)[:-1]
ret = 'git+%s' % (origin,)
if include_commit:
ret += '#commit=%s' % (commit,)
return ret
