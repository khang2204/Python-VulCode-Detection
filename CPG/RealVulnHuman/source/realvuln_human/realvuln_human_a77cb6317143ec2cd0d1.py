return 'no updates available'

def resolve_system_diagnostics(self, info, username, password, cmd='whoami'):
  q = User.query.filter_by(username='admin').first()
  real_passw = q.password
  res, msg = security.check_creds(username, password, real_passw)
  Audit.create_audit_entry(info)
  if res:
    output = f'{cmd}: command not found'
    if security.allowed_cmds(cmd):
      output = helpers.run_cmd(cmd)
    return output
  return msg

def resolve_system_debug(self, info, arg=None):
  Audit.create_audit_entry(info)
  if arg:
    output = helpers.run_cmd('ps {}'.format(arg))
  else:
    output = helpers.run_cmd('ps')
  return output
