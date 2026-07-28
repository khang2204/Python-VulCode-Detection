queryset2 = User.query.all()
    items.extend(queryset2)
  return items

def resolve_pastes(self, info, public=False, limit=1000, filter=None):
  query = PasteObject.get_query(info)
  Audit.create_audit_entry(info)
  result = query.filter_by(public=public, burn=False)

  if filter:
    result = result.filter(text("title = '%s' or content = '%s'" % (filter, filter)))

  return result.order_by(Paste.id.desc()).limit(limit)

def resolve_paste(self, info, id=None, title=None):
  query = PasteObject.get_query(info)
  Audit.create_audit_entry(info)
  if title:
    return query.filter_by(title=title, burn=False).first()

  return query.filter_by(id=id, burn=False).first()
