@staticmethod...
user = UserService.get_user_by_username(username)
stats_dto = UserStatsDTO()
actions = TaskHistory.query.filter(TaskHistory.user_id == user.id, 
    TaskHistory.action_text != '').all()
tasks_mapped = TaskHistory.query.filter(TaskHistory.user_id == user.id, 
    TaskHistory.action_text == 'MAPPED').count()
tasks_validated = TaskHistory.query.filter(TaskHistory.user_id == user.id, 
    TaskHistory.action_text == 'VALIDATED').count()
projects_mapped = TaskHistory.query.filter(TaskHistory.user_id == user.id, 
    TaskHistory.action == 'STATE_CHANGE').distinct(TaskHistory.project_id
    ).count()
stats_dto.tasks_mapped = tasks_mapped
stats_dto.tasks_validated = tasks_validated
stats_dto.projects_mapped = projects_mapped
stats_dto.total_time_spent = 0
stats_dto.time_spent_mapping = 0
stats_dto.time_spent_validating = 0
sql = (
    """SELECT SUM(TO_TIMESTAMP(action_text, 'HH24:MI:SS')::TIME) FROM task_history
                WHERE action='LOCKED_FOR_VALIDATION'
                and user_id = {0};"""
    .format(user.id))
total_validation_time = db.engine.execute(sql)
for time in total_validation_time:
total_validation_time = time[0]
sql = (
    """SELECT SUM(TO_TIMESTAMP(action_text, 'HH24:MI:SS')::TIME) FROM task_history
                WHERE action='LOCKED_FOR_MAPPING'
                and user_id = {0};"""
    .format(user.id))
if total_validation_time:
total_mapping_time = db.engine.execute(sql)
stats_dto.time_spent_validating = total_validation_time.total_seconds()
for time in total_mapping_time:
stats_dto.total_time_spent += stats_dto.time_spent_validating
total_mapping_time = time[0]
return stats_dto
if total_mapping_time:
stats_dto.time_spent_mapping = total_mapping_time.total_seconds()
stats_dto.total_time_spent += stats_dto.time_spent_mapping
