@user_passes_test(user_is_superuser)...
projects = Project.objects.all()
for project in projects:
create_testcases_celery.delay(project.id)
return redirect('testcases:testcases')
