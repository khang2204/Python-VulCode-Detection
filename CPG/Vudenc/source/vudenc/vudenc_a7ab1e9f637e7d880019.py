def invalidate_members(sender, instance, reverse=False, **kwargs):...
if reverse:
CachedTopMenu.invalidate(instance.user)
for profile in instance.members.all():
CachedTopMenu.invalidate(profile.user)
