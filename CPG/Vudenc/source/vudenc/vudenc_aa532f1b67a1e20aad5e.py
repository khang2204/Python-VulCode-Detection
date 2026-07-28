@register.inclusion_tag('exercise/_submission_list.html', takes_context=True)...
submissions = context['profile'].submissions.filter(
    exercise__course_module__course_instance=context['instance']).order_by(
    '-id')[:10]
return {'submissions': submissions, 'title': _('Latest submissions'),
    'empty': _('No submissions for this course.')}
