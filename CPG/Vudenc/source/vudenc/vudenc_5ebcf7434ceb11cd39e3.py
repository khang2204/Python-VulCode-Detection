@user_passes_test(user_is_staff)...
"""docstring"""
testrail_contents = push_testcases_to_testrail_celery.delay(project_id)
context = context_testcases()
context['testrail'] = testrail_contents
context['link_id'] = project_id
return render(request, 'testcases/testcases.html', context)
