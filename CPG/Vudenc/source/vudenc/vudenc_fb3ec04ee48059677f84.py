def set_pending_action(self, pending_action, request, pk=None, project_pk=...
get_and_check_project(request, project_pk, perms)
task = self.queryset.get(pk=pk, project=project_pk)
task.pending_action = pending_action
task.last_error = None
task.save()
scheduler.process_pending_tasks(background=True)
return Response({'success': True})
