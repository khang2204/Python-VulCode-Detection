def __init__(self, request):...
self.request = request
self.target_field = request.POST.get('target_field')
self.new_value = request.POST.get('new_value')
