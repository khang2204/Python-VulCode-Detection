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
