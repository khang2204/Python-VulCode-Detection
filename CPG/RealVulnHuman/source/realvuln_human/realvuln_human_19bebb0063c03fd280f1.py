return HttpResponse("Error: no email inputted")

# Set password variable
if 'password' in request.POST:
    password = request.POST['password']
elif password is None:
    return HttpResponse("Error: no password inputted")

message = ""
try:
    response = HttpResponseRedirect(path)
    user = User.authenticate(email, password)
    if 'remember' in request.POST:
        year_in_sec = 365 * 24 * 60 * 60
        response.set_cookie("auth_token", user.auth_token,
                            max_age=year_in_sec)
    else:
        response.set_cookie("auth_token", user.auth_token)
    return response
except User.DoesNotExist:
    message = "Email incorrect!"
