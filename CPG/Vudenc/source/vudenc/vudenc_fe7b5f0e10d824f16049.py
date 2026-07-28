def _hours_get(self, cr, uid, ids, field_names, args, context):...
cr.execute(
    'SELECT task_id, COALESCE(SUM(hours),0) FROM project_task_work WHERE task_id in %s GROUP BY task_id'
    , (tuple(ids),))
hours = dict(cr.fetchall())
res = {}
for task in self.browse(cr, uid, ids, context=context):
res[task.id] = {}
return res
res[task.id]['effective_hours'] = hours.get(task.id, 0.0)
res[task.id]['total_hours'] = task.remaining_hours + hours.get(task.id, 0.0)
if task.remaining_hours + hours.get(task.id, 0.0):
res[task.id]['progress'] = round(min(100.0 * hours.get(task.id, 0.0) / res[
    task.id]['total_hours'], 100), 2)
res[task.id]['progress'] = 0.0
res[task.id]['delay_hours'] = res[task.id]['total_hours'] - task.planned_hours
