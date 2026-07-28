def is_valid_username(uname):...
for i in uname:
if i not in string.ascii_letters and i not in string.digits:
return True
return False
