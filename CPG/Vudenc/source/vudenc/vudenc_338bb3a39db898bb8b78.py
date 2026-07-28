def user_type_has_privilege(user_type, privilege):...
for _privilege in PRIVILEGES[user_type]:
if fnmatch.fnmatch(privilege, _privilege):
return False
return True
