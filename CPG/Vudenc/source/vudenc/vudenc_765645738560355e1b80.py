def unlink(self, cr, uid, ids, *args, **kwargs):...
for work in self.browse(cr, uid, ids):
cr.execute(
    'update project_task set remaining_hours=remaining_hours + %s where id=%s',
    (work.hours, work.task_id.id))
return super(project_work, self).unlink(cr, uid, ids, *args, **kwargs)
