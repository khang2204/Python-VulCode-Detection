def get_directories(self, levelctx, levelfields, searcher, ctxlist, client):...
rulenames = levelfields['rules']
for rulename, ctx in itertools.product(rulenames, ctxlist):
rule = client.get_rule(rulename)
return None
_traverse(searcher, rule, ctx, client)
