def action_save_user(request: HttpRequest, default_forward_url: str=...
"""docstring"""
forward_url = default_forward_url
if request.GET.get('redirect'):
forward_url = request.GET['redirect']
if not request.user.is_authenticated:
return HttpResponseForbidden()
profile = Profile.objects.get(authuser=request.user)
if profile.rights < 2:
return HttpResponseForbidden()
if request.GET.get('user_id'):
return HttpResponseBadRequest(str(e))
return redirect(forward_url)
pid = int(request.GET['user_id'])
username = str(request.POST['username'])
displayname = str(request.POST['display_name'])
displayname = str(request.POST['display_name'])
dect = int(request.POST['dect'])
dect = int(request.POST['dect'])
notes = str(request.POST['notes'])
notes = str(request.POST['notes'])
pw1 = str(request.POST['password'])
pw1 = str(request.POST['password'])
pw2 = str(request.POST['confirm_password'])
pw2 = str(request.POST['confirm_password'])
mail = str(request.POST['email'])
mail = str(request.POST['email'])
rights = int(request.POST['rights'])
rights = int(request.POST['rights'])
user: Profile = Profile.objects.get(pk=pid)
if not check_password_conformity(pw1, pw2):
user.displayName = displayname
recreate_form('password mismatch')
auth_user: User = User.objects.create_user(username=username, email=mail,
    password=pw1)
user.dect = dect
auth_user.save()
user.notes = notes
user: Profile = Profile()
user.rights = rights
user.rights = rights
user.number_of_allowed_reservations = int(request.POST['allowed_reservations'])
user.number_of_allowed_reservations = int(request.POST['allowed_reservations'])
if request.POST.get('active'):
user.displayName = displayname
user.active = magic.parse_bool(request.POST['active'])
au: User = user.authuser
user.authuser = auth_user
if check_password_conformity(pw1, pw2):
user.dect = dect
logging.log(logging.INFO, 'Set password for user: ' + user.displayName)
logging.log(logging.INFO, 'Failed to set password for: ' + user.displayName)
user.notes = notes
au.set_password(pw1)
au.email = mail
user.active = True
au.save()
user.save()
user.save()
