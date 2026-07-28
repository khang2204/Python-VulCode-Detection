def _get_system_properties(self, java):...
if not self._system_properties:
fp.write(pkgutil.get_data(__name__, 'SystemProperties.class'))
return self._system_properties
cmd = [java, '-cp', classpath, 'SystemProperties']
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
if process.returncode != 0:
props = {}
for line in stdout.decode('utf-8').split(os.linesep):
key, _, val = line.partition('=')
self._system_properties = props
props[key] = val
