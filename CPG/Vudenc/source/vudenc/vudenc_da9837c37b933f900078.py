@with_timeout...
transport = ssh.get_transport()
chan = transport.open_session()
chan.invoke_shell()
LOG.debug(_('Reading CLI MOTD'))
self._get_output(chan)
cmd = 'stty columns 255'
LOG.debug(_("Setting CLI terminal width: '%s'"), cmd)
chan.send(cmd + '\r')
out = self._get_output(chan)
LOG.debug(_("Sending CLI command: '%s'"), command)
chan.send(command + '\r')
out = self._get_output(chan)
chan.close()
if any(line.startswith(('% Error', 'Error:')) for line in out):
desc = _('Error executing EQL command')
return out
cmdout = '\n'.join(out)
LOG.error(cmdout)
