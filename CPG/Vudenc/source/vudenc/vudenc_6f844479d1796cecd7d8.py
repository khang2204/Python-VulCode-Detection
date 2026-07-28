def _load_sos_presets(self):...
cmd = self.host.prefix + 'sosreport --list-presets'
res = self.run_command(cmd)
if res['status'] == 0:
for line in res['stdout'].splitlines():
if line.strip().startswith('name:'):
pname = line.split('name:')[1].strip()
self.sos_info['presets'].append(pname)
