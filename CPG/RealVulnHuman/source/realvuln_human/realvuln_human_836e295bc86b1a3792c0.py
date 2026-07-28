except:
            pass

        return HttpResponseRedirect(reverse('app:login'))


@require_http_methods(["POST"])
def reset_password(request):
    if request.POST.get('user', '') != '':
        encoded_user = request.POST['user']
        user = pickle.loads(base64.b64decode(encoded_user))
        user.password = request.POST['password']
        user.save()
        messages.success(request, 'Your password has been updated')
    else:
        try:
            messages.error(request, 'Password did not reset')
        except:
            pass

    return redirect('/login')
