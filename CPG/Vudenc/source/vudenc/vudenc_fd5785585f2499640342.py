def login(request):...
if request.user.is_authenticated():
next_url = request.GET.get('next', reverse('home'))
logger.error('login() - got anonymous user: %s' % request.META)
return HttpResponseRedirect(next_url)
return HttpResponseServerError(
    'Internet Server error. Please contact %s for assistance.' % BDR_EMAIL)
