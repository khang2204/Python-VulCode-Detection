@staticmethod...
"""docstring"""
if new_state in [TaskStatus.READY, TaskStatus.LOCKED_FOR_VALIDATION,
return
project = ProjectService.get_project_by_id(project_id)
user = UserService.get_user_by_id(user_id)
StatsService._update_tasks_stats(project, user, last_state, new_state, action)
UserService.upsert_mapped_projects(user_id, project_id)
project.last_updated = timestamp()
return project, user
