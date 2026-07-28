'available_receipients': User.objects.all()
            })


# W0613 = unused-argument
@require_http_methods(["GET", "DELETE"])
@user_is_authenticated
def user_message(request, user_id, message_id):  # pylint: disable=W0613
    current_user = utils.current_user(request)
    try:
        message = Message.objects.get(pk=message_id)
        if request.method == "GET":
            return render(request, "users/messages/show.html", {
                'current_user': current_user,
                'message': message
            })
        else:
            message.delete()
            return HttpResponse("Success!")
    except Exception:
        return redirect("/users/" + str(current_user.id) + "/messages")
