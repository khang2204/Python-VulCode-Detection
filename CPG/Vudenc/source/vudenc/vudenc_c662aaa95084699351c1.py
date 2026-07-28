def get_directories(self, levelctx, levelfields, searcher, ctxlist, client):...
doexisting = searcher.do_existing_paths()
dirlist = []
if doexisting:
for ictx in ctxlist:
values = []
ctxdirs = glob.glob(os.path.join(ictx.path, '*'))
return dirlist
if 'key' in levelfields:
ctxdirs = (x for x in ctxdirs if os.path.isdir(x))
search_param = searcher.get_parameters(levelfields['key'], levelctx, ctxlist)
if 'collection' in levelfields:
if 'collection' in levelfields:
if search_param:
coll = client.get_collection(levelfields['collection'])
for ctx, value in itertools.product(ctxlist, values):
coll = client.get_collection(levelfields['collection'])
dirlist.extend((ictx, x) for x in ctxdirs)
values.extend(x for x in search_param if x)
bad_values = [x for x in values if x not in coll]
dirlist.append((ctx, os.path.join(ctx.path, value)))
ctxdirs = (x for x in ctxdirs if os.path.split(x)[-1] in coll)
if bad_values:
