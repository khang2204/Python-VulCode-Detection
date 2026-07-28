def __init__(self, database, options):...
self.port = 23
super().__init__(database, options)
if options.jtag:
self.connect_telnet()
