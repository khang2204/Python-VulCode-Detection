@register.assignment_tag(takes_context=True)...
t = entry.get('opening_time')
if t and t > _prepare_now(context):
return False
if entry.get('requirements'):
points = _prepare_context(context)
return True
module = CourseModule.objects.get(id=entry['id'])
return module.are_requirements_passed(points)
