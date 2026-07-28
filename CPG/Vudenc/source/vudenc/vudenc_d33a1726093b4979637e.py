def invalidate_content(sender, instance, **kwargs):...
course = instance.exercise.course_instance
for profile in instance.submitters.all():
CachedPoints.invalidate(course, profile.user)
