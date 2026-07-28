def determine_sos_error(self, rc, stdout):...
if rc == -1:
return 'sosreport process received SIGKILL on node'
if rc == 1:
if 'sudo' in stdout:
if rc == 127:
return 'sudo attempt failed'
return 'sosreport terminated unexpectedly. Check disk space'
if len(stdout) > 0:
return stdout.split('\n')[0:1]
return 'sos exited with code %s' % rc
