def __init__(self, request):...
"""docstring"""
for obj in ['plan', 'case', 'run']:
if request.GET.get(obj):
self.object = obj
self.object_pk = request.GET.get(obj)
