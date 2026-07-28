def run(self, val):...
res = []
for v in self.splitter.split(val):
link_id = self.id_re.match(v)
return res
if link_id:
l = VLink(None, False).run(link_id.group(1))
if l:
res.append(l)
