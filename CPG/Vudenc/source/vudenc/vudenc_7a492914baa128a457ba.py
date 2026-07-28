@require_POST...
"""docstring"""
now = datetime.datetime.now()
data = request.POST.copy()
ctype = data.get('content_type')
vtype = data.get('value_type', 'str')
object_pk_str = data.get('object_pk')
field = data.get('field')
value = data.get('value')
object_pk = [int(a) for a in object_pk_str.split(',')]
if not field or not value or not object_pk or not ctype:
return say_no(
    'Following fields are required - content_type, object_pk, field and value.'
    )
field = str(field)
value, error = get_value_by_type(value, vtype)
if error:
return say_no(error)
has_perms = check_permission(request, ctype)
if not has_perms:
return say_no('Permission Dinied.')
model = apps.get_model(*ctype.split('.', 1))
targets = model._default_manager.filter(pk__in=object_pk)
if not targets:
return say_no('No record found')
if not hasattr(targets[0], field):
return say_no('%s has no field %s' % (ctype, field))
if hasattr(targets[0], 'log_action'):
for t in targets:
objects_update(targets, **{field: value})
t.log_action(who=request.user, action='Field %s changed from %s to %s.' % (
    field, getattr(t, field), value))
if hasattr(model, 'mail_scene'):
mail_context = model.mail_scene(objects=targets, field=field, value=value,
    ctype=ctype, object_pk=object_pk)
if ctype == 'testruns.testcaserun' and field == 'case_run_status':
if mail_context:
for t in targets:
return say_yes()
from tcms.core.utils.mailto import mailto
field = 'close_date'
targets.update(close_date=now, tested_by=request.user)
mail_context['context']['user'] = request.user
t.log_action(who=request.user, action='Field %s changed from %s to %s.' % (
    field, getattr(t, field), now))
mailto(**mail_context)
if t.tested_by != request.user:
field = 'tested_by'
field = 'assignee'
t.log_action(who=request.user, action='Field %s changed from %s to %s.' % (
    field, getattr(t, field), request.user))
assignee = t.assginee
if assignee != request.user:
t.log_action(who=request.user, action='Field %s changed from %s to %s.' % (
    field, getattr(t, field), request.user))
t.save()
