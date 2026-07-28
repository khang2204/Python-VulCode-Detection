@detail_route(methods=['get'])...
"""docstring"""
get_and_check_project(request, project_pk)
task = self.queryset.get(pk=pk, project=project_pk)
line_num = max(0, int(request.query_params.get('line', 0)))
output = task.console_output or ''
return Response('\n'.join(output.split('\n')[line_num:]))
