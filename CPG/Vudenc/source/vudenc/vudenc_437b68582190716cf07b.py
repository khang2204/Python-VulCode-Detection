def get_fw_path(src, dst, rtype='TEXT', verbose=True):...
"""docstring"""
rtypes = 'TEXT', 'TREE', 'JSON', 'YAML', 'NGTREE'
if rtype in rtypes:
logcmd = nglib.config['nglib']['logcmd']
logurl = nglib.config['nglib']['logurl']
srcnet = nglib.query.net.find_cidr(src)
dstnet = nglib.query.net.find_cidr(dst)
logger.info('Query: Security Path %s -> %s for %s', src, dst, nglib.user)
if nglib.verbose:
print("""
Finding security path from {:} -> {:}:
""".format(srcnet, dstnet))
path = nglib.py2neo_ses.cypher.execute(
    'MATCH (s:Network { cidr:{src} })-[e1:VRF_IN]->(sv:VRF), ' +
    '(d:Network {cidr:{dst}})-[e2:VRF_IN]->(dv:VRF), ' +
    'p = shortestPath((sv)-[:VRF_IN|ROUTED_FW|:SWITCHED_FW*0..20]-(dv)) RETURN s,d,p'
    , src=srcnet, dst=dstnet)
fwsearch = dict()
ngtree = nglib.ngtree.get_ngtree('Security Path', tree_type='L4-PATH')
if len(path) > 0:
for r in path.records:
sn = r.s
ngtree = nglib.query.exp_ngtree(ngtree, rtype)
snp = nglib.query.nNode.getJSONProperties(sn)
return ngtree
dn = r.d
dnp = nglib.query.nNode.getJSONProperties(dn)
startpath = snp['cidr'] + ' -> '
path = ''
nodes = r.p.nodes
for node in nodes:
nProp = nglib.query.nNode.getJSONProperties(node)
ngtree['Name'] = re.search('(.*)\\s->\\s$', path).group(1)
label = nglib.query.nNode.getLabel(node)
path = snp['cidr'] + ' -> ' + path + dnp['cidr']
tlabel = re.search('(\\w+)', label)
if rtype == 'TEXT':
hop = nglib.ngtree.get_ngtree(tlabel.group(1), tree_type='L4-HOP')
print('\nSecurity Path: ' + path)
print()
if re.search('VRF', label):
for fw in fwsearch.keys():
path = path + 'VRF:' + nProp['name'] + ' -> '
if re.search('FW', label):
hostname, logIndex = fwsearch[fw].split(',')
path = path + nProp['name'] + ' -> '
for prop in nProp:
cmd = "{:} 'index={:} host::{:} {:} {:}'".format(logcmd, logIndex, hostname,
    src, dst)
fwsearch[nProp['name']] = nProp['hostname'] + ',' + nProp['logIndex']
hop[prop] = nProp[prop]
nglib.ngtree.add_child_ngtree(ngtree, hop)
query = 'index={:} host::{:} {:} {:}'.format(logIndex, hostname, src, dst)
hop['Name'] = 'FW'
query = query.replace(' ', '%20')
print("""
{:} (15min): {:}{:}""".format(fw, logurl, query))
if verbose:
print(cmd)
proc = subprocess.Popen([cmd + ' 2> /dev/null'], stdout=subprocess.PIPE,
    shell=True, universal_newlines=True)
out, err = proc.communicate()
if err:
print(err)
if out:
print(out)
