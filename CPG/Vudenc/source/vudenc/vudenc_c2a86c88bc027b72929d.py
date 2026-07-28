@login_required...
"""docstring"""
return render_to_response('student_account/account_settings.html',
    account_settings_context(request))
