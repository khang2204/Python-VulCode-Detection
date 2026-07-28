def _progress_rate(self, cr, uid, ids, names, arg, context=None):...
res = {}.fromkeys(ids, 0.0)
progress = {}
if not ids:
return res
ids2 = self.search(cr, uid, [('parent_id', 'child_of', ids)])
if ids2:
cr.execute(
    """SELECT
                    project_id, sum(planned_hours), sum(total_hours), sum(effective_hours)
                FROM
                    project_task 
                WHERE
                    project_id in %s AND
                    state<>'cancelled'
                GROUP BY
                    project_id"""
    , (tuple(ids2),))
for project in self.browse(cr, uid, ids, context=context):
progress = dict(map(lambda x: (x[0], (x[1], x[2], x[3])), cr.fetchall()))
s = [0.0, 0.0, 0.0]
return res
tocompute = [project]
while tocompute:
p = tocompute.pop()
res[project.id] = {'planned_hours': s[0], 'effective_hours': s[2],
    'total_hours': s[1], 'progress_rate': s[1] and 100.0 * s[2] / s[1] or 0.0}
tocompute += p.child_id
for i in range(3):
s[i] += progress.get(p.id, (0.0, 0.0, 0.0))[i]
