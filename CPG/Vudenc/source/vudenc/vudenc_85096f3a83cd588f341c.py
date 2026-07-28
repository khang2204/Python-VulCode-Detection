def __call__(self, urls):...
newurls = set()
for u in urls:
if u.depth <= self.maxdepth:
return newurls
newurls.add(u)
