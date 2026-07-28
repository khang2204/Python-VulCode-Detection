def read_params(self, get_params=None, post_params=None, file_params=None):...
"""docstring"""
if self.request.method == 'GET':
if get_params:
if post_params:
for key, validator in get_params.items():
for key, validator in post_params.items():
if file_params:
if key in self.request.GET:
if key in self.request.POST:
for key, validator in file_params.items():
setattr(self.params, key, validator(self.request.GET[key]))
setattr(self.params, key, validator(self.request.POST[key]))
if key in self.request.FILES:
setattr(self.params, key, validator(self.request.FILES[key]))
