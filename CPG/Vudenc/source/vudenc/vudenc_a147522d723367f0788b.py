def _prepare_context(context, student=None):...
if not 'instance' in context:
instance = context['instance']
_prepare_now(context)
if not 'content' in context:
context['content'] = CachedContent(instance)
def points(user, key):...
if not key in context:
context[key] = CachedPoints(instance, user, context['content'])
return context[key]
