def create(self, cr, uid, vals, *args, **kwargs):...
if 'hours' in vals and not vals['hours']:
vals['hours'] = 0.0
if 'task_id' in vals:
cr.execute(
    'update project_task set remaining_hours=remaining_hours - %s where id=%s',
    (vals.get('hours', 0.0), vals['task_id']))
return super(project_work, self).create(cr, uid, vals, *args, **kwargs)
