@register.inclusion_tag('exercise/_user_last.html', takes_context=True)...
user = context['request'].user
points = _prepare_context(context)
if user.is_authenticated():
last = LearningObjectDisplay.objects.filter(profile=user.userprofile,
    learning_object__status=LearningObject.STATUS.READY,
    learning_object__course_module__course_instance=context['instance']
    ).select_related('learning_object').order_by('-timestamp').first()
return {'begin': points.begin(), 'instance': context['instance']}
if last:
entry, _, _, _ = points.find(last.learning_object)
return {'last': entry, 'last_time': last.timestamp}
