def subprocess_execute(cmd):...
import subprocess
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    shell=True, universal_newlines=True)
stdout, stderr = p.communicate()
output = stdout.splitlines()
return output, stderr
