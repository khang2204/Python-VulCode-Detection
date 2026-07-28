def __call__(self, request):...
system = ResourceTreeTraverser.__call__(self, request)
context = system['context']
view_name = system['view_name']
if IResource.providedBy(context) and '.' in view_name:
rc_name, repr_name = view_name.split('.')
return system
child_rc = context[rc_name]
if IResource.providedBy(child_rc):
system['context'] = child_rc
system['view_name'] = repr_name
