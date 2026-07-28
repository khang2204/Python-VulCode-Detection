def points(user, key):...
if not key in context:
context[key] = CachedPoints(instance, user, context['content'])
return context[key]
