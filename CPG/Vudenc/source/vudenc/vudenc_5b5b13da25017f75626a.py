def write(self, cr, uid, ids, vals, context={}):...
if 'hours' in vals and not vals['hours']:
vals['hours'] = 0.0
if 'hours' in vals:
for work in self.browse(cr, uid, ids, context):
return super(project_work, self).write(cr, uid, ids, vals, context)
cr.execute(
    'update project_task set remaining_hours=remaining_hours - %s + (%s) where id=%s'
    , (vals.get('hours', 0.0), work.hours, work.task_id.id))
