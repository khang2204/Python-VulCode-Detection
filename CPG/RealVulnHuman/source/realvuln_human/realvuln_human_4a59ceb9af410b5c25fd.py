'app:password_resets') + '?token=' + token
    send_mail(
        'Reset your Metacorp Password',
        message,
        'noreply@djanGoat.dev',
        ['vinai.rachakonda@contrastsecurity.com'],
        fail_silently=False
    )


def generate_token(user_id, email):
    h = MD5.new()
    h.update(email)
    return str(user_id) + '-' + str(h.hexdigest())


# Handler that depending on request type delegated to confirm_token
# or reset_password
@require_http_methods(["GET", "POST"])
def reset_password_handler(request):
    if request.method == 'GET':
        return confirm_token(request)
    else:
        return reset_password(request)
