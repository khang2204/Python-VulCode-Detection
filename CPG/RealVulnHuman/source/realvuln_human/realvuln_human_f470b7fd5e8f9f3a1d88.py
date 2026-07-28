def resolve_paste(self, info, id=None, title=None):
  query = PasteObject.get_query(info)
  Audit.create_audit_entry(info)
  if title:
    return query.filter_by(title=title, burn=False).first()

  return query.filter_by(id=id, burn=False).first()

def resolve_system_update(self, info):
  security.simulate_load()
  Audit.create_audit_entry(info)
  return 'no updates available'

def resolve_system_diagnostics(self, info, username, password, cmd='whoami'):
  q = User.query.filter_by(username='admin').first()
  real_passw = q.password
  res, msg = security.check_creds(username, password, real_passw)
  Audit.create_audit_entry(info)
  if res:
    output = f'{cmd}: command not found'
    if security.allowed_cmds(cmd):
