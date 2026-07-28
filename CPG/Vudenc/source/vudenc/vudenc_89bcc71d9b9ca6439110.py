@user_passes_test(user_is_superuser)...
testrail = get_object_or_404(TestRailConfiguration, pk=testrail_id)
testrail.delete()
context = context_project_dashboard(request)
context['last_tab'] = 'test_rails'
return render(request, 'projects/project_dashboard.html', context)
