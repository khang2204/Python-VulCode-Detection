def unlink(self, cr, uid, ids, *args, **kwargs):...
for proj in self.browse(cr, uid, ids):
if proj.tasks:
return super(project, self).unlink(cr, uid, ids, *args, **kwargs)
