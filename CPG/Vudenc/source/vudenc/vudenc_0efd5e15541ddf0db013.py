def check_celery_task_state(request):...
task_run = False
active = celery_app.control.inspect().active()
key = 'celery@' + socket.gethostname() + '.mdta'
if active[key]:
task_run = True
return HttpResponse(json.dumps(task_run), content_type='application/json')
project_id = active[key][0]['args']
project_id = ''.join(c for c in project_id if c not in "'(),")
if int(project_id) == request.user.humanresource.project.id:
task_run = True
