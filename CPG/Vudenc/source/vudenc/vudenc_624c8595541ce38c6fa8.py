def shell(self, params):...
if params == 'id -u':
return b'root'
if params == 'bugreportz':
if self.fail_br:
if params == 'bugreportz -v':
return b'OMG I died!\n'
return b'OK:/path/bugreport.zip\n'
if self.fail_br_before_N:
return b'/system/bin/sh: bugreportz: not found'
return b'1.1'
