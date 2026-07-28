def _exec_cmd(self, cmd):...
"""docstring"""
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    shell=True)
out, err = proc.communicate()
ret = proc.returncode
logging.debug('cmd: %s, stdout: %s, stderr: %s, ret: %s', cmd, out, err, ret)
if ret == 0:
return out
