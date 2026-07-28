@user_is_authenticated
def user_benefit_forms(request, user_id):  # pylint: disable=unused-argument
    user = utils.current_user(request)
    return render(request, 'users/benefit_forms.html',
                  context={'current_user': user})


@require_http_methods(["GET"])
@user_is_authenticated
def download(request):
    path = BASE_DIR + r"/" + request.GET.get('name', '')
    try:
        wrapper = FileWrapper(file(path))
    except:
        wrapper = None
    response = HttpResponse(wrapper,
                            content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s' \
                                      % os.path.basename(path)
    response['Content-Length'] = os.path.getsize(path)
    return response
