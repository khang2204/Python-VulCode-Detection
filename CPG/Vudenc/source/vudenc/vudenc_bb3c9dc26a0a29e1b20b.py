def get_rule_attributes(levellist, doc):...
ret = set()
for level in levellist:
leveltype = level[0]
return ret
levelfields = level[1]
ret |= FnLevel[leveltype].get_attributes(levelfields, doc)
