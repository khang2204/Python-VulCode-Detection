def __init__(self, serial=''):...
self.serial = serial
if serial:
self.adb_str = 'adb -s %s' % serial
self.adb_str = 'adb'
