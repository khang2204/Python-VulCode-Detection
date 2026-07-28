def create_message(self, request):...
"""docstring"""
if not self.is_mine(request):
user = request.user
user.message_set.create(message=self.message_template % self.created_at)
