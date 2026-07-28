def index(request):
    if request.method == "POST":
        form = request.POST
        if not form:
            return HttpResponse("Users index")
        err_msg = User.validate_signup_form(form)
        if len(err_msg) > 0:
            messages.add_message(request, messages.INFO, err_msg)
        else:
            try:
                user = User.objects.create(email=form["email"],
                                           password=form["password"],
                                           is_admin=False,
                                           first_name=form["first_name"],
                                           last_name=form["last_name"],
                                           created_at=timezone.now(),
                                           updated_at=timezone.now(),
                                           )
                user.build_benefits_data()
                auth = User.authenticate(form["email"], form["password"])
                response = redirect("/dashboard/home", permanent=False)
                response.set_cookie('auth_token', auth.auth_token)
