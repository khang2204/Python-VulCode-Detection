@require_http_methods(['POST'])...
"""docstring"""
limiter = BadRequestRateLimiter()
if limiter.is_rate_limit_exceeded(request):
AUDIT_LOG.warning('Password reset rate limit exceeded')
user = request.user
return HttpResponseForbidden()
email = user.email if user.is_authenticated() else request.POST.get('email')
if email:
return HttpResponseBadRequest(_('No email address provided.'))
request_password_change(email, request.is_secure())
AUDIT_LOG.info('Invalid password reset attempt')
return HttpResponse(status=200)
user = user if user.is_authenticated() else User.objects.get(email=email)
limiter.tick_bad_request_counter(request)
destroy_oauth_tokens(user)
