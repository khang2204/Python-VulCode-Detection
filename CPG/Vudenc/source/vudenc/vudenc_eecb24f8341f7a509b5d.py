def tags(request):...
"""docstring"""
tag_objects = _TagObjects(request)
template_name, obj = tag_objects.get()
q_tag = request.GET.get('tags')
q_action = request.GET.get('a')
if q_action:
tag_actions = _TagActions(obj=obj, tag_name=q_tag)
all_tags = obj.tag.all().order_by('pk')
getattr(tag_actions, q_action)()
test_plan_tags = TestPlanTag.objects.filter(tag__in=all_tags).values('tag'
    ).annotate(num_plans=Count('tag')).order_by('tag')
test_case_tags = TestCaseTag.objects.filter(tag__in=all_tags).values('tag'
    ).annotate(num_cases=Count('tag')).order_by('tag')
test_run_tags = TestRunTag.objects.filter(tag__in=all_tags).values('tag'
    ).annotate(num_runs=Count('tag')).order_by('tag')
plan_counter = _TagCounter('num_plans', test_plan_tags)
case_counter = _TagCounter('num_cases', test_case_tags)
run_counter = _TagCounter('num_runs', test_run_tags)
for tag in all_tags:
tag.num_plans = plan_counter.calculate_tag_count(tag)
context_data = {'tags': all_tags, 'object': obj}
tag.num_cases = case_counter.calculate_tag_count(tag)
return render(request, template_name, context_data)
tag.num_runs = run_counter.calculate_tag_count(tag)
