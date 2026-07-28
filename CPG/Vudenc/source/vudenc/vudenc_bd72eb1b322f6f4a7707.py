def get_context_data(self, **kwargs):...
context = super().get_context_data(**kwargs)
context['is_mobile'] = is_mobile(self.request.META['HTTP_USER_AGENT'])
return context
