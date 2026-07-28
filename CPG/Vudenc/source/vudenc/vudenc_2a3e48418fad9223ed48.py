def get_and_check_project(request, project_pk, perms=('view_project',)):...
"""docstring"""
project = models.Project.objects.get(pk=project_pk, deleting=False)
return project
for perm in perms:
if not request.user.has_perm(perm, project):
