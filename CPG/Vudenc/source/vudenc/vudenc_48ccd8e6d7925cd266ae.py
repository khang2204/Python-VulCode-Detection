def harvest_contest_data(contest_id):...
"""docstring"""
users = {}
tasks = []
contest = Contest.get_from_id(contest_id, session)
for participation in contest.participations:
user = participation.user
for task in contest.tasks:
users[user.username] = {'password': user.password}
tasks.append((task.id, task.name, task.statements.keys()))
return users, tasks
