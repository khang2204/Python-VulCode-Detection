user = User.objects.get(user_id=int(selected_id))
        data = request.POST.dict().copy()
        if data:
            password = data['password']
            data.pop('password')
            data.pop('password_confirmation')
            data['updated_at'] = pytz.utc.localize(datetime.datetime.now())
            if password != '':
                user.password = password
                user.save()
        User.objects.filter(user_id=int(selected_id)).update(**data)
    except User.DoesNotExist:
        success = False

    msg = "success" if success else "failure"
    return JsonResponse({'msg': msg})


@require_http_methods(["GET"])
@user_is_authenticated
def admin_get_all_users(request, selected_id):  # pylint: disable=unused-argument
