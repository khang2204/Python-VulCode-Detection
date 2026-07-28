def getprop(self, params):...
if params == 'ro.build.id':
return 'AB42'
if params == 'ro.build.type':
return 'userdebug'
if params == 'ro.build.product' or params == 'ro.product.name':
return 'FakeModel'
if params == 'sys.boot_completed':
return '1'
