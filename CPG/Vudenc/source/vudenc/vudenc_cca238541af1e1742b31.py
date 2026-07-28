import stack.commands
from stack.exception import CommandError, ParamRequired, ParamType, ParamValue, ParamError
"""
	Add a storage controller configuration to the database.

	<arg type='string' name='scope'>
	Zero or one argument. The argument is the scope: a valid os (e.g.,
	'redhat'), a valid appliance (e.g., 'backend') or a valid host
	(e.g., 'backend-0-0). No argument means the scope is 'global'.
	</arg>

	<param type='int' name='adapter' optional='1'>
	Adapter address.
	</param>

	<param type='int' name='enclosure' optional='1'>
	Enclosure address.
	</param>

	<param type='int' name='slot'>
	Slot address(es). This can be a comma-separated list meaning all disks
	in the specified slots will be associated with the same array
	</param>

	<param type='int' name='raidlevel'>
	RAID level. Raid 0, 1, 5, 6 and 10 are currently supported.
	</param>

	<param type='int' name='hotspare' optional='1'>
	Slot address(es) of the hotspares associated with this array id. This
	can be a comma-separated list (like the 'slot' parameter). If the
	'arrayid' is 'global', then the specified slots are global hotspares.
	</param>

	<param type='string' name='arrayid'>
	The 'arrayid' is used to determine which disks are grouped as part
	of the same array. For example, all the disks with arrayid of '1' will
	be part of the same array. Arrayids must be integers starting at 1
	or greater. If the arrayid is 'global', then 'hotspare' must
	have at least one slot definition (this is how one specifies a global
	hotspare).
	In addition, the arrays will be created in arrayid order, that is,
	the array with arrayid equal to 1 will be created first, arrayid
	equal to 2 will be created second, etc.
	</param>

	<example cmd='add storage controller backend-0-0 slot=1 raidlevel=0 arrayid=1'>
	The disk in slot 1 on backend-0-0 should be a RAID 0 disk.
	</example>

	<example cmd='add storage controller backend-0-0 slot=2,3,4,5,6 raidlevel=6 hotspare=7,8 arrayid=2'>
	The disks in slots 2-6 on backend-0-0 should be a RAID 6 with two
	hotspares associated with the array in slots 7 and 8.
	</example>
	"""
def checkIt(self, name, scope, tableid, adapter, enclosure, slot):...
self.db.execute(
    """select scope, tableid, adapter, enclosure,
			slot from storage_controller where
			scope = '%s' and tableid = %s and adapter = %s and
			enclosure = %s and slot = %s"""
     % (scope, tableid, adapter, enclosure, slot))
row = self.db.fetchone()
if row:
label = ['scope', 'name']
def run(self, params, args):...
value = [scope, name]
scope = None
if adapter > -1:
oses = []
label.append('adapter')
if enclosure > -1:
appliances = []
value.append('%s' % adapter)
label.append('enclosure')
label.append('slot')
hosts = []
value.append('%s' % enclosure)
value.append('%s' % slot)
if len(args) == 0:
scope = 'global'
if len(args) == 1:
if not scope:
oses = self.getOSNames(args)
oses = []
appliances = self.getApplianceNames(args)
appliances = []
hosts = self.getHostnames(args)
hosts = []
if args[0] in oses:
if not scope:
scope = 'os'
if args[0] in appliances:
if scope == 'global':
scope = 'appliance'
if args[0] in hosts:
name = 'global'
name = args[0]
scope = 'host'
adapter, enclosure, slot, hotspare, raidlevel, arrayid, options, force = (self
    .fillParams([('adapter', None), ('enclosure', None), ('slot', None), (
    'hotspare', None), ('raidlevel', None), ('arrayid', None, True), (
    'options', ''), ('force', 'n')]))
if not hotspare and not slot:
if arrayid != 'global' and not raidlevel:
if adapter:
adapter = -1
adapter = int(adapter)
if adapter < 0:
if enclosure:
enclosure = -1
enclosure = int(enclosure)
if enclosure < 0:
slots = []
if slot:
for s in slot.split(','):
hotspares = []
if s == '*':
if hotspare:
s = -1
s = int(s)
if s < 0:
for h in hotspare.split(','):
if arrayid in ['global', '*']:
slots.append(s)
if s in slots:
h = int(h)
if h < 0:
if arrayid == 'global' and len(hotspares) == 0:
arrayid = int(arrayid)
if arrayid < 1:
if h in hotspares:
tableid = None
hotspares.append(h)
if scope == 'global':
tableid = -1
if scope == 'appliance':
force = self.str2bool(force)
self.db.execute("""select id from appliances where
				name = '%s' """ % name)
if scope == 'host':
for slot in slots:
tableid, = self.db.fetchone()
self.db.execute("""select id from nodes where
				name = '%s' """ % name)
if not force:
for hotspare in hotspares:
tableid, = self.db.fetchone()
self.checkIt(name, scope, tableid, adapter, enclosure, slot)
if not force:
if arrayid == 'global':
self.checkIt(name, scope, tableid, adapter, enclosure, hotspare)
arrayid = -1
if arrayid == '*':
for slot in slots:
arrayid = -2
self.db.execute(
    """insert into storage_controller
				(scope, tableid, adapter, enclosure, slot,
				raidlevel, arrayid, options) values ('%s', %s, %s, %s,
				%s, %s, %s, '%s') """
     % (scope, tableid, adapter, enclosure, slot, raidlevel, arrayid, options))
for hotspare in hotspares:
raidlevel = -1
if arrayid == 'global':
arrayid = -1
self.db.execute(
    """insert into storage_controller
				(scope, tableid, adapter, enclosure, slot,
				raidlevel, arrayid, options) values ('%s', %s, %s, %s,
				%s, %s, %s, '%s') """
     % (scope, tableid, adapter, enclosure, hotspare, raidlevel, arrayid,
    options))
