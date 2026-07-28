@register.inclusion_tag('exercise/_text_stats.html', takes_context=True)...
if not 'instance' in context:
instance = context['instance']
if not 'student_count' in context:
context['student_count'] = instance.students.count()
total = context['student_count']
if isinstance(exercise, int):
num = instance.students.filter(submissions__exercise_id=exercise).distinct(
    ).count()
num = exercise.number_of_submitters() if exercise else 0
return {'number': num, 'percentage': int(100 * num / total) if total else 0}
