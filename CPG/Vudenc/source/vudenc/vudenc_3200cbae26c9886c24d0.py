def __call__(self, url):...
a = []
if self.param:
for p in utils.tup(self.param):
return self.run(*a)
if self.post and request.post.get(p):
val = request.post[p]
if self.get and request.get.get(p):
a.append(val)
val = request.get[p]
if self.url and url.get(p):
val = url[p]
val = self.default
