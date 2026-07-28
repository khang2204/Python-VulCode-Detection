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
value = [scope, name]
if adapter > -1:
label.append('adapter')
if enclosure > -1:
value.append('%s' % adapter)
label.append('enclosure')
label.append('slot')
value.append('%s' % enclosure)
value.append('%s' % slot)
