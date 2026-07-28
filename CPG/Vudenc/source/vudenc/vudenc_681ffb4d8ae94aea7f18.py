def run(self, params, args):...
attr, doc = self.fillParams([('attr', None, True), ('doc', None, True)])
rows = self.db.execute(
    """
			select attr from attributes where attr='%s'
			""" % attr)
if not rows:
self.db.execute("""
			delete from attributes_doc where attr='%s'
			""" % attr
    )
if doc:
self.db.execute(
    """
				insert into attributes_doc
				(attr, doc)
				values ('%s', '%s')
				"""
     % (attr, doc))
