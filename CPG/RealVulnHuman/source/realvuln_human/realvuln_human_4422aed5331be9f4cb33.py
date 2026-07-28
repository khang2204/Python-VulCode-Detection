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


@require_http_methods(["GET"])
def confirm_token(request):
    if request.GET.get('token', '') != '' and is_valid_token(
            request.GET['token']):
        messages.success(request, 'Please create a new password.')
        user_id = request.GET['token'].split('-')[0]
        user = User.objects.filter(user_id=user_id).first()
        encoded = base64.b64encode(pickle.dumps(user))
