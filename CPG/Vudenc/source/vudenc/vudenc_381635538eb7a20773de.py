def notification_entry(n):...
exercise = n.submission.exercise if n.submission else None
return {'id': n.id, 'submission_id': n.submission.id if n.submission else 0,
    'name': '{} {}, {}'.format(n.course_instance.course.code, str(exercise.
    parent) if exercise and exercise.parent else n.course_instance.
    instance_name, str(exercise) if exercise else n.subject), 'link': n.
    get_display_url()}
