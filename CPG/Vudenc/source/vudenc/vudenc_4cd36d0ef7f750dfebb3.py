def new(local, remote='', dir_index=False, modify=False, handler=FileHandler):...
if local.endswith('/'):
local = local[:-1]
if remote.endswith('/'):
remote = remote[:-1]
if modify:
inherit = ModifyMixIn, handler
inherit = handler,
def respond(self):...
norm_request = normpath(self.groups['path'])
if self.groups['path'] != norm_request:
self.response.headers.set('Location', self.remote + norm_request)
self.filename = self.local + urllib.parse.unquote(self.groups['path'])
return 307, ''
return handler.respond(self)
