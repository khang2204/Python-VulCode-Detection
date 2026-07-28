def run_command(self, cmd, timeout=180, get_pty=False, need_root=False):...
"""docstring"""
if cmd.startswith('sosreport'):
cmd = cmd.replace('sosreport', self.host.sos_bin_path)
if need_root:
need_root = True
get_pty = True
self.log_debug('Running command %s' % cmd)
cmd = self._format_cmd(cmd)
if 'atomic' in cmd:
get_pty = True
if not self.local:
now = time.time()
proc = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
sin, sout, serr = self.client.exec_command(cmd, timeout=timeout, get_pty=
    get_pty)
if self.config['become_root'] and need_root:
while time.time() < now + timeout:
stdout, stderr = proc.communicate(input=self.config['root_password'] + '\n')
if self.config['need_sudo'] and need_root:
if not sout.channel.exit_status_ready():
rc = proc.returncode
stdout, stderr = proc.communicate(input=self.config['sudo_pw'] + '\n')
stdout, stderr = proc.communicate()
time.sleep(0.1)
if sout.channel.exit_status_ready():
return self._fmt_output(stdout=stdout, stderr=stderr, rc=rc)
if self.config['become_root'] and need_root:
rc = sout.channel.recv_exit_status()
sin.write(self.config['root_password'] + '\n')
if self.config['sudo_pw'] and need_root:
return self._fmt_output(sout, serr, rc)
sin.flush()
sin.write(self.config['sudo_pw'] + '\n')
need_root = False
sin.flush()
need_root = False
