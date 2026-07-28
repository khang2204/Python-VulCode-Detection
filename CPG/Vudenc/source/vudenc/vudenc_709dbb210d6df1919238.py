def _complete_name(self, cr, uid, ids, name, args, context):...
res = {}
for m in self.browse(cr, uid, ids, context=context):
res[m.id] = (m.parent_id and m.parent_id.name + '/' or '') + m.name
return res
