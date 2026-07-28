@staticmethod...
"""docstring"""
base = db.session.query(User.id, User.username, User.mapping_level, User.role)
if query.mapping_level:
base = base.filter(User.mapping_level == MappingLevel[query.mapping_level.
    upper()].value)
if query.username:
base = base.filter(User.username.ilike(query.username.lower() + '%'))
if query.role:
base = base.filter(User.role == UserRole[query.role.upper()].value)
results = base.order_by(User.username).paginate(query.page, 20, True)
dto = UserSearchDTO()
for result in results.items:
listed_user = ListedUser()
dto.pagination = Pagination(results)
listed_user.id = result.id
return dto
listed_user.mapping_level = MappingLevel(result.mapping_level).name
listed_user.username = result.username
listed_user.role = UserRole(result.role).name
dto.users.append(listed_user)
