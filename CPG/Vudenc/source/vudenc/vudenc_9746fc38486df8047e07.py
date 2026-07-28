def do_open(self, cr, uid, ids, *args):...
tasks = self.browse(cr, uid, ids)
for t in tasks:
self.write(cr, uid, [t.id], {'state': 'open'})
return True
