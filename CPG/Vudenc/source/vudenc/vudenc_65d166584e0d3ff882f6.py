def check_permission(request, ctype):...
perm = '%s.change_%s' % tuple(ctype.split('.'))
if request.user.has_perm(perm):
return True
return False
