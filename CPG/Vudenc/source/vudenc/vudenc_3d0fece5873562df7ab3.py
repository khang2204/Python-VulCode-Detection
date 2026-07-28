def invalidate_notification(sender, instance, **kwargs):...
course = instance.course_instance
if not course and instance.submission:
course = instance.submission.exercise.course_instance
CachedPoints.invalidate(course, instance.recipient.user)
