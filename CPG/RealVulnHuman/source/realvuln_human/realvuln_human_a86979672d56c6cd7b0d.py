from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from app.models.User.user import User
from app.models.Analytics.analytics import Analytics
from app.views import utils
from app.decorators import user_is_authenticated


@require_http_methods(["GET"])
@user_is_authenticated
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
