def get_or_create_tag(session, tagname):...
instance = Tag.query.filter_by(name=tagname).first()
if instance:
return instance, False
created = datetime.utcnow()
instance = Tag(name=tagname, created=created)
session.add(instance)
return instance, True
