query = UserObject.get_query(info)

  result = query.filter_by(username=identity).first()
  return result

def resolve_search(self, info, keyword=None):
  Audit.create_audit_entry(info)
  items = []
  if keyword:
    search = "%{}%".format(keyword)
    queryset1 = Paste.query.filter(Paste.title.like(search))
    items.extend(queryset1)
    queryset2 = User.query.filter(User.username.like(search))
    items.extend(queryset2)
  else:
    queryset1 = Paste.query.all()
    items.extend(queryset1)
    queryset2 = User.query.all()
    items.extend(queryset2)
  return items
