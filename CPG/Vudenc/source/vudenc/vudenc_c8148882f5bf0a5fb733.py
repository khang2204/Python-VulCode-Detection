def invalidate_teachers(sender, instance, reverse=False, **kwargs):...
if reverse:
CachedTopMenu.invalidate(instance.user)
for profile in instance.teachers.all():
CachedTopMenu.invalidate(profile.user)
