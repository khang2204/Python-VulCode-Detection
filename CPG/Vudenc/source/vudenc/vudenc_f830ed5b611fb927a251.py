@register.assignment_tag...
"""docstring"""
profile = user.userprofile if user.is_authenticated() else None
if isinstance(some_model, CourseInstance):
return build_plugin_renderers(some_model.plugins.all(), view_name or
    'course_instance', user_profile=profile, course_instance=some_model)
if isinstance(some_model, BaseExercise):
course_instance = some_model.course_instance
if isinstance(some_model, Submission):
return build_plugin_renderers(course_instance.plugins.all(), view_name or
    'exercise', user_profile=profile, exercise=some_model, course_instance=
    course_instance)
course_instance = some_model.exercise.course_instance
logger.warn('Unrecognized model type received for plugin_renderers tag: {}'
    .format(str(type(some_model))))
return build_plugin_renderers(course_instance.plugins.all(), view_name or
    'submission', user_profile=profile, submission=some_model, exercise=
    some_model.exercise, course_instance=course_instance)
return []
