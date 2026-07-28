@login_required...
"""docstring"""
return render_to_response('student_account/finish_auth.html', {
    'disable_courseware_js': True, 'disable_footer': True})
