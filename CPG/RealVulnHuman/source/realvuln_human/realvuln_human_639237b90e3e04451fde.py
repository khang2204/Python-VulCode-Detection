from django.shortcuts import render, redirect
from django.core.mail import send_mail
from app.models import User
from Crypto.Hash import MD5
import pickle
import base64


@require_http_methods(["POST"])
def forgot_password(request):
    qset = User.objects.filter(email=request.POST.get('email', ''))
    if len(qset) > 0:
        user = qset.first()
        messages.success(request, 'An email was sent to reset your password!')
        password_reset_mailer(request, user)
    else:
        try:
            messages.error(request, 'We do not have the email in our system')
        except:
            pass

    return redirect('/login')


def password_reset_mailer(request, user):  # pylint: disable=unused-argument
    token = generate_token(user.user_id, user.email)
    message = 'Use this link: ' + 'localhost:8000' + reverse(
        'app:password_resets') + '?token=' + token
