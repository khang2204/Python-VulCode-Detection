@staticmethod...
"""docstring"""
results = db.session.query(TaskHistory.id, TaskHistory.task_id, TaskHistory
    .action, TaskHistory.action_date, TaskHistory.action_text, User.username
    ).join(User).filter(TaskHistory.project_id == project_id, TaskHistory.
    action != 'COMMENT').order_by(TaskHistory.action_date.desc()).paginate(page
    , 10, True)
if results.total == 0:
activity_dto = ProjectActivityDTO()
for item in results.items:
history = TaskHistoryDTO()
activity_dto.pagination = Pagination(results)
history.history_id = item.id
return activity_dto
history.task_id = item.task_id
history.action = item.action
history.action_text = item.action_text
history.action_date = item.action_date
history.action_by = item.username
activity_dto.activity.append(history)
