@register.inclusion_tag('exercise/_user_results.html', takes_context=True)...
values = _get_toc(context, student)
values['total_json'] = json.dumps(values['total'])
if student:
values['is_course_staff'] = False
return values
