def run(self, title):...
if not title:
c.errors.add(errors.NO_TITLE)
if len(title) > 100:
c.errors.add(errors.TITLE_TOO_LONG)
return title
