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

def resolve_read_and_burn(self, info, id):
  result = Paste.query.filter_by(id=id, burn=True).first()
  Paste.query.filter_by(id=id, burn=True).delete()
  db.session.commit()
  Audit.create_audit_entry(info)
  return result
