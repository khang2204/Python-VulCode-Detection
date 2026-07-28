def validate(self, tok):...
id = tok.value.upper()
if tok.type == 'ID':
if not id in self.spdx.licenses:
if tok.type == 'EXC':
self.lastid = id
if id not in self.spdx.exceptions:
if tok.type != 'WITH':
if self.lastid not in self.spdx.exceptions[id]:
self.lastid = None
self.lastid = None
