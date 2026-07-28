db.session.commit()
  Audit.create_audit_entry(info)
  return result

def resolve_system_health(self, info):
  Audit.create_audit_entry(info)
  return 'System Load: {}'.format(
    helpers.run_cmd("uptime | awk -F': ' '{print $2}' | awk -F',' '{print $1}'")
  )

def resolve_users(self, info, id=None):
  query = UserObject.get_query(info)
  Audit.create_audit_entry(info)
  if id:
    result = query.filter_by(id=id)
  else:
    result = query

  return result

def resolve_audits(self, info):
  query = Audit.query.all()
  Audit.create_audit_entry(info)
  return query

def resolve_delete_all_pastes(self, info):
  Audit.create_audit_entry(info)
  Paste.query.delete()
  db.session.commit()
