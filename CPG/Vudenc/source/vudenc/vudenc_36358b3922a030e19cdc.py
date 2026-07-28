def _get_toc(context, student=None):...
points = _prepare_context(context, student)
context = context.flatten()
context.update({'modules': points.modules_flatted(), 'categories': points.
    categories(), 'total': points.total(), 'is_course_staff': context.get(
    'is_course_staff', False)})
return context
