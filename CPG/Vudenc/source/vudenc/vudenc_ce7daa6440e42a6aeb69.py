def run(self, title):...
title = VLength.run(self, title)
if title and self.only_whitespace.match(title):
c.errors.add(errors.NO_TITLE)
return title
