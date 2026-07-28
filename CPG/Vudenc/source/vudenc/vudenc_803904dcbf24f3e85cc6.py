def get_bookmarks(self, levelfields, doc):...
bookmarks = set()
rulenames = levelfields['rules']
for rulename in rulenames:
rule = doc['rules'][rulename]
return bookmarks
bookmarks |= get_rule_bookmarks(rule, doc)
