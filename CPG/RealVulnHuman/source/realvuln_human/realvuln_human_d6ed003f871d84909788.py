other_is_admin_val = False
    else:
        other_is_admin_val = not user.is_admin

    return render(request, 'admin/modal.html',
                  {'user': user, 'other_admin_val': other_is_admin_val})


@require_http_methods(["DELETE"])
@user_is_authenticated
def admin_delete_user(request, selected_id):  # pylint: disable=unused-argument
    success = True
    try:
        user = User.objects.get(user_id=int(selected_id))
        user.delete()
    except User.DoesNotExist:
        success = False

    msg = "success" if success else "failure"
    return JsonResponse({'msg': msg})


@require_http_methods(["POST", "PATCH"])
@user_is_authenticated
def admin_update_user(request, selected_id):
    success = True
    try:
        user = User.objects.get(user_id=int(selected_id))
        data = request.POST.dict().copy()
        if data:
