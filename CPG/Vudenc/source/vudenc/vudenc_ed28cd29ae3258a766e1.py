@staticmethod...
"""docstring"""
results = db.session.query(User.username, User.projects_mapped.any(
    project_id).label('participant')).filter(User.username.ilike(
    user_filter.lower() + '%')).order_by(desc('participant').nullslast(),
    User.username).paginate(page, 20, True)
if results.total == 0:
dto = UserFilterDTO()
for result in results.items:
dto.usernames.append(result.username)
dto.pagination = Pagination(results)
if project_id is not None:
return dto
participant = ProjectParticipantUser()
participant.username = result.username
participant.project_id = project_id
participant.is_participant = bool(result.participant)
dto.users.append(participant)
