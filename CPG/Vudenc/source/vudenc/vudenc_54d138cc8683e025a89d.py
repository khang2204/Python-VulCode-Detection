def get_directories(self, levelctx, levelfields, searcher, ctxlist, client):...
candidates = [(x, os.path.join(x.path, levelfields['name'])) for x in ctxlist]
if searcher.do_existing_paths():
candidates = [(x, y) for x, y in candidates if os.path.isdir(y)]
return candidates
