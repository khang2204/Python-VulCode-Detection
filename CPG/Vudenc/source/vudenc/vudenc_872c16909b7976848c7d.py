def _prepare_now(context):...
if not 'now' in context:
context['now'] = timezone.now()
return context['now']
