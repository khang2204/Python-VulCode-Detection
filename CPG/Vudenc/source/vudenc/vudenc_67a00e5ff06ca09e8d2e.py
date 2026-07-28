def get_full_routed_path(src, dst, rtype='NGTREE', l2path=False):...
"""docstring"""
rtypes = 'CSV', 'TREE', 'JSON', 'YAML', 'NGTREE'
if rtype in rtypes:
srct, dstt, ngtree = None, None, None
if re.search('^\\d+\\.\\d+\\.\\d+\\.\\d+$', src):
srct = nglib.query.net.get_net(src, rtype='NGTREE')
if re.search('^\\d+\\.\\d+\\.\\d+\\.\\d+$', dst):
dstt = nglib.query.net.get_net(dst, rtype='NGTREE')
if srct['_child001']['VRF'] == dstt['_child001']['VRF']:
ngtree = get_routed_path(src, dst, verbose=False)
secpath = get_fw_path(src, dst, rtype='NGTREE')
return ngtree
ngtree = nglib.ngtree.get_ngtree(secpath['Name'], tree_type='L4-PATH')
first = True
last = None
for key in sorted(secpath.keys()):
if '_child' in key:
if last:
if re.search('(Network|FW)', secpath[key]['Name']):
rtree = get_routed_path(secpath[last]['gateway'], dst, vrf=dstt['_child001'
    ]['VRF'], l2path=l2path)
if first:
if rtree:
rtree = get_routed_path(src, secpath[key]['gateway'], vrf=srct['_child001']
    ['VRF'], l2path=l2path)
nglib.ngtree.add_child_ngtree(ngtree, secpath[key])
nglib.ngtree.add_child_ngtree(ngtree, rtree)
if rtree:
last = key
nglib.ngtree.add_child_ngtree(ngtree, rtree)
first = False
