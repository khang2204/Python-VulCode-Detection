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
                return response
            except Exception as e:
                messages.add_message(request, messages.INFO, str(e))
        return HttpResponseRedirect("/signup/")

    else:
        return HttpResponse("Users index")


@require_http_methods(["GET"])
