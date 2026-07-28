def __make_proxy(self, method_name, data, args, options):...
reg = get_current_registry()
adp = reg.queryAdapter(data, IDataTraversalProxyAdapter)
if not adp is None:
prx = getattr(adp, method_name)(*args, **options)
if not isinstance(data, (MutableSequence, MutableSet)):
return prx
prxs = []
for item in data:
adp = reg.queryAdapter(item, IDataTraversalProxyAdapter)
prx = DataSequenceTraversalProxy(prxs)
if adp is None:
prx = getattr(adp, method_name)(*args, **options)
prxs.append(prx)
