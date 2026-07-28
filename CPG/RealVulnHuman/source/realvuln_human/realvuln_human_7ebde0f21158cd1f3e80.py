def admin_dashboard(request, selected_id):  # pylint: disable=unused-argument
    current_user = utils.current_user(request)
    return render(request, 'admin/dashboard.html', {'current_user': current_user})


@require_http_methods(["GET"])
@user_is_authenticated
def admin_get_user(request, selected_id):
    user = None
    try:
        user = User.objects.get(user_id=int(selected_id))
    except User.DoesNotExist:
        return render(request, 'admin/modal_notFound.html')

    if user is None:
        other_is_admin_val = False
    else:
        other_is_admin_val = not user.is_admin

    return render(request, 'admin/modal.html',
                  {'user': user, 'other_admin_val': other_is_admin_val})
