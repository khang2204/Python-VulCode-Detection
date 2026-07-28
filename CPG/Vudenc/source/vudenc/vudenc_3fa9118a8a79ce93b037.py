def dispatch(self, request, *args, **kwargs):...
logger.debug(f'{self.__class__.__name__} access check')
if (self.access_granted or self.access_form_valid
return self._redirect_from_passphrase(request)
if self.access_granted or self.access_form_valid:
return super().dispatch(request, *args, **kwargs)
return self._render_access_form()
