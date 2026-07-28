def add_comment_count(self, result):...
for r in result:
if not r.name:
r._comment_count = 0
if '_comments' in r:
r._comment_count = len(json.loads(r._comments or '[]'))
