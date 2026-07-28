def fields_view_get(self, cr, uid, view_id=None, view_type='form', context=...
tm = self.pool.get('res.users').browse(cr, uid, uid, context
    ).company_id.project_time_mode or False
f = self.pool.get('res.company').fields_get(cr, uid, ['project_time_mode'],
    context)
word = 'Hours'
if tm:
word = dict(f['project_time_mode']['selection'])[tm]
res = super(task, self).fields_view_get(cr, uid, view_id, view_type,
    context, toolbar)
if not tm or tm == 'hours':
return res
eview = etree.fromstring(res['arch'])
def _check_rec(eview, tm):...
if eview.attrib.get('widget', False) == 'float_time':
eview.set('widget', 'float')
for child in eview:
_check_rec(child, tm)
return True
