def str2bool(value):...
v = value.lower()
if v in ('yes', 'true', 't', '1', 'y'):
return True
if v in ('no', 'false', 'f', 'n', '0'):
return False
