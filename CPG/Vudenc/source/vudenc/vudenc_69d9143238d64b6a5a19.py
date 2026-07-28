def invalidate_assistants(sender, instance, reverse=False, **kwargs):...
if reverse:
CachedTopMenu.invalidate(instance.user)
for profile in instance.assistants.all():
CachedTopMenu.invalidate(profile.user)
