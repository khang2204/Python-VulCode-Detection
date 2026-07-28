def get_form_kwargs(self):...
kwargs = super().get_form_kwargs()
kwargs.update({'view': self})
return kwargs
