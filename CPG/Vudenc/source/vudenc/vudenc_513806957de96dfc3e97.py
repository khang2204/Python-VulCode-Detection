def duplicate_template(self, cr, uid, ids, context={}):...
default = {'parent_id': context.get('parent_id', False)}
for id in ids:
self.copy(cr, uid, id, default=default)
cr.commit()
