def form_valid(self, form):...
logger.debug(f'{self.__class__.__name__} form valid')
output = super().form_valid(form)
self.view_action()
return output
