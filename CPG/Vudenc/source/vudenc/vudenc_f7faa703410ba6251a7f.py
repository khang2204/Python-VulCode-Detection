import stack.commands
from stack.exception import ArgError, ParamValue
"""
	List the storage controller configuration for one of the following:
	global, os, appliance or host.

	<arg optional='1' type='string' name='host'>
	This argument can be nothing, a valid 'os' (e.g., 'redhat'), a valid
	appliance (e.g., 'backend') or a host.
	If nothing is supplied, then the global storage controller
	configuration will be output.
	</arg>

	<example cmd='list storage controller backend-0-0'>
	List host-specific storage controller configuration for backend-0-0.
	</example>

	<example cmd='list storage controller backend'>
	List appliance-specific storage controller configuration for all
	backend appliances.
	</example>

	<example cmd='list storage controller'>
	List global storage controller configuration for all hosts.
	</example>

	"""
def run(self, params, args):...
scope = None
oses = []
appliances = []
hosts = []
if len(args) == 0:
scope = 'global'
if len(args) == 1:
if not scope:
oses = self.getOSNames(args)
oses = []
appliances = self.getApplianceNames()
appliances = []
hosts = self.getHostnames()
hosts = []
if args[0] in oses:
if not scope:
scope = 'os'
if args[0] in appliances:
query = None
scope = 'appliance'
if args[0] in hosts:
if scope == 'global':
scope = 'host'
query = """select adapter, enclosure, slot, raidlevel,
				arrayid, options from storage_controller 
				where scope = 'global'
				order by enclosure, adapter, slot"""
if scope == 'os':
if not query:
return
if scope == 'appliance':
return
name = None
query = (
    """select adapter, enclosure, slot,
				raidlevel, arrayid, options
				from storage_controller where
				scope = "appliance" and tableid = (select
				id from appliances
				where name = '%s')
				order by enclosure, adapter, slot"""
     % args[0])
if scope == 'host':
if scope == 'global':
query = (
    """select adapter, enclosure, slot,
				raidlevel, arrayid, options
				from storage_controller where
				scope = "host" and tableid = (select
				id from nodes where name = '%s')
				order by enclosure, adapter, slot"""
     % args[0])
name = 'global'
if scope in ['appliance', 'host']:
self.beginOutput()
name = args[0]
self.db.execute(query)
i = 0
for row in self.db.fetchall():
adapter, enclosure, slot, raidlevel, arrayid, options = row
self.endOutput(header=['scope', 'enclosure', 'adapter', 'slot', 'raidlevel',
    'arrayid', 'options'], trimOwner=False)
if i > 0:
name = None
if adapter == -1:
adapter = None
if enclosure == -1:
enclosure = None
if slot == -1:
slot = '*'
if raidlevel == '-1':
raidlevel = 'hotspare'
if arrayid == -1:
arrayid = 'global'
if arrayid == -2:
options = options.strip('"')
arrayid = '*'
self.addOutput(name, [enclosure, adapter, slot, raidlevel, arrayid, options])
i += 1
