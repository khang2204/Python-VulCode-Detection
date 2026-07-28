"""netgrph is the primary CLI query too for NetGrph
   Also see ngreport
"""
import os
import re
import argparse
import nglib
import nglib.query
config_file = '/etc/netgrph.ini'
alt_config = './docs/netgrph.ini'
dirname = os.path.dirname(os.path.realpath(__file__))
if re.search('\\/dev$', dirname):
config_file = 'netgrphdev.ini'
if re.search('\\/test$', dirname):
parser = argparse.ArgumentParser()
config_file = 'netgrphdev.ini'
parser = argparse.ArgumentParser(prog='netgrph', description=
    'Query the NetGrph Database', epilog=
    """
                                 Examples:
                                 netgrph 10.1.1.1 (Free Search for IP),
                                 netgrph -net 10.1.1.0/24 (Search for CIDR),
                                 netgrph -group MDC (VLAN Database Search),
                                 netgrph -fp 10.1.1.1 10.2.2.1 (Firewall Path Search)
                                 """
    )
parser.add_argument('search', help=
    'Search the NetGrph Database (Wildcard Default)', type=str)
parser.add_argument('-ip', help='Network Details for an IP', action=
    'store_true')
parser.add_argument('-net', help=
    'All networks within a CIDR (eg. 10.0.0.0/8)', action='store_true')
parser.add_argument('-nlist', help='Get all networks in an alert group',
    action='store_true')
parser.add_argument('-nfilter', help=
    'Get all networks on a filter (see netgrph.ini)', action='store_true')
parser.add_argument('-dev', help=
    'Get the Details for a Device (Switch/Router/FW)', action='store_true')
parser.add_argument('-path', metavar='src', help=
    'Full Path Between -p src dst (ip/cidr, requires NetDB)', type=str)
parser.add_argument('-fpath', metavar='src', help=
    'Security Path between -fp src dst', type=str)
parser.add_argument('-rpath', metavar='src', help=
    'Routed Path between -rp IP/CIDR1 IP/CIDR2 ', type=str)
parser.add_argument('-spath', metavar='src', help=
    'Switched Path between -sp sw1 sw2 (Neo4j Regex)', type=str)
parser.add_argument('-group', help='Get VLANs for a Management Group',
    action='store_true')
parser.add_argument('-vrange', metavar='1[-4096]', help=
    'VLAN Range (default 1-1999)', type=str)
parser.add_argument('-vid', help='VLAN ID Search', action='store_true')
parser.add_argument('-vtree', help='Get the VLAN Tree for a VNAME', action=
    'store_true')
parser.add_argument('-output', metavar='TREE', help=
    'Return Format: TREE, TABLE, CSV, JSON, YAML', type=str)
parser.add_argument('--days', metavar='int', help=
    'Days in Past (NetDB Specific)', type=int)
parser.add_argument('--conf', metavar='file', help='Alternate Config File',
    type=str)
parser.add_argument('--debug', help='Set debugging level', type=int)
parser.add_argument('--verbose', help='Verbose Output', action='store_true')
args = parser.parse_args()
if args.conf:
config_file = args.conf
if not os.path.exists(config_file):
if not os.path.exists(alt_config):
verbose = 0
config_file = alt_config
if args.verbose:
verbose = 1
if args.debug:
verbose = args.debug
if not args.days:
args.days = 7
if not args.vrange:
args.vrange = '1-1999'
if args.output:
args.output = args.output.upper()
nglib.verbose = verbose
nglib.init_nglib(config_file)
if args.fpath:
nglib.query.path.get_fw_path(args.fpath, args.search)
if args.spath:
rtype = 'TREE'
if args.rpath:
if args.output:
rtype = 'TREE'
if args.path:
rtype = args.output
nglib.query.path.get_switched_path(args.spath, args.search, rtype=rtype)
if args.output:
rtype = 'TREE'
if args.dev:
rtype = args.output
nglib.query.path.get_routed_path(args.rpath, args.search, rtype=rtype)
if args.output:
rtype = 'TREE'
if args.ip:
rtype = args.output
nglib.query.path.get_full_path(args.path, args.search, rtype=rtype)
if args.output:
rtype = 'TREE'
if args.net:
rtype = args.output
nglib.query.dev.get_device(args.search, rtype=rtype, vrange=args.vrange)
if args.output:
rtype = 'CSV'
if args.nlist:
rtype = args.output
nglib.query.net.get_net(args.search, rtype=rtype, days=args.days)
if args.output:
rtype = 'CSV'
if args.nfilter:
rtype = args.output
nglib.query.net.get_networks_on_cidr(args.search, rtype=rtype)
if args.output:
rtype = 'CSV'
if args.group:
rtype = args.output
nglib.query.net.get_networks_on_filter(args.search, rtype=rtype)
if args.output:
nglib.query.vlan.get_vlans_on_group(args.search, args.vrange)
if args.vtree:
rtype = args.output
nglib.query.net.get_networks_on_filter(nFilter=args.search, rtype=rtype)
rtype = 'TREE'
if args.vid:
if args.output:
rtype = 'TREE'
if args.search:
rtype = args.output
nglib.query.vlan.get_vtree(args.search, rtype=rtype)
if args.output:
vid = re.search('^(\\d+)$', args.search)
parser.print_help()
rtype = args.output
nglib.query.vlan.search_vlan_id(args.search, rtype=rtype)
vname = re.search('^(\\w+\\-\\d+)$', args.search)
print()
ip = re.search('^(\\d+\\.\\d+\\.\\d+\\.\\d+)$', args.search)
net = re.search('^(\\d+\\.\\d+\\.\\d+\\.\\d+\\/\\d+)$', args.search)
text = re.search('^(\\w+)$', args.search)
if vid:
if vname:
if int(args.search) >= 0 and int(args.search) <= 4096:
rtype = 'TREE'
if net:
rtype = 'TREE'
if args.output:
rtype = 'CSV'
if ip:
if args.output:
rtype = args.output
nglib.query.vlan.get_vtree(args.search, rtype=rtype)
if args.output:
rtype = 'TREE'
if text:
rtype = args.output
nglib.query.vlan.search_vlan_id(args.search, rtype=rtype)
rtype = args.output
nglib.query.net.get_networks_on_cidr(args.search, rtype=rtype)
if args.output:
rtype = 'TREE'
print('Unknown Search:', args.search)
rtype = args.output
nglib.query.net.get_net(args.search, rtype=rtype, days=args.days)
if args.output:
rtype = args.output
nglib.query.universal_text_search(args.search, args.vrange, rtype=rtype)
