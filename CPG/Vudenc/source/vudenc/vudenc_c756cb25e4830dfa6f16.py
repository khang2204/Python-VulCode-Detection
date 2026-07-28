def getChild(self, path, request):...
if path == '':
return self
if path == 'login':
return self
if not self.is_logged_in(request):
return UnAuthorizedResource()
return NoResource()
